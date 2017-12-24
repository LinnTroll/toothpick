from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets, serializers

from core.models import Toothpick, ToothpickOwnership


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class OwnerListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(toothpickownership__enabled=True)
        return super(OwnerListSerializer, self).to_representation(data)


class OwnerSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        list_serializer_class = OwnerListSerializer


class OwnerHistorySerializer(serializers.ModelSerializer):
    user = BaseUserSerializer()

    class Meta:
        model = ToothpickOwnership
        fields = ('own_start_at', 'own_end_at', 'user')


class ToothpickSerializer(serializers.ModelSerializer):
    owners = OwnerSerializer(many=True, read_only=True)
    owners_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    owners_history = OwnerHistorySerializer(source='toothpickownership_set', many=True, read_only=True)

    def validate_owners_ids(self, value):
        request_ids = set(value)
        valid_ids = set(User.objects.filter(pk__in=value).values_list('id', flat=True))
        invalid_ids = request_ids - valid_ids
        if invalid_ids:
            raise serializers.ValidationError('Wrong ids: {}'.format(invalid_ids))
        return value

    def _process_ownership_create(self, instance, create_ids):
        for user_id in create_ids:
            ownership = ToothpickOwnership(
                toothpick=instance,
                user_id=user_id,
            )
            ownership.save()

    def _process_ownership_delete(self, instance, delete_ids):
        if delete_ids:
            ownerships = ToothpickOwnership.objects.filter(
                toothpick=instance,
                user_id__in=delete_ids,
                enabled=True,
            )
            for ownership in ownerships:
                ownership.enabled = None
                ownership.own_end_at = timezone.now()
                ownership.save()

    def create(self, validated_data):
        create_ids = set(validated_data.pop('owners_ids'))
        instance = super(ToothpickSerializer, self).create(validated_data)
        self._process_ownership_create(instance, create_ids)
        return instance

    def update(self, instance, validated_data):
        new_ids = set(validated_data.pop('owners_ids'))
        instance = super(ToothpickSerializer, self).update(instance, validated_data)
        exists_ids = set(u.id for u in instance.actual_owners())
        create_ids = new_ids - exists_ids
        delete_ids = exists_ids - new_ids
        self._process_ownership_create(instance, create_ids)
        self._process_ownership_delete(instance, delete_ids)
        return instance

    class Meta:
        model = Toothpick
        fields = ('id', 'serial_number', 'name', 'owners', 'owners_ids', 'owners_history')


class ToothpickViewSet(viewsets.ModelViewSet):
    queryset = Toothpick.objects.all()
    serializer_class = ToothpickSerializer
    http_method_names = ['get', 'post', 'put', 'options']


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    http_method_names = ['get', 'options']

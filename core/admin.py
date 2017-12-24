from django.contrib import admin

from core.models import Toothpick, ToothpickOwnership


class ToothpickOwnershipInline(admin.TabularInline):
    model = ToothpickOwnership
    readonly_fields = ('user', 'enabled', 'own_start_at', 'own_end_at')
    extra = 0
    max_num = 0
    can_delete = False


class ToothpickAdmin(admin.ModelAdmin):
    def get_owners(self, item):
        return [u.username for u in item.actual_owners()]

    get_owners.short_description = 'owners'
    list_display = ('name', 'get_owners', 'created_at')
    inlines = (ToothpickOwnershipInline,)


admin.site.register(Toothpick, ToothpickAdmin)

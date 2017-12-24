def cors_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, PATCH, HEAD"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return middleware

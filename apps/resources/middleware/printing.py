

def printing_middleware(get_response):
    def middleware(request):
        # pre-processing
        print("pre-processing message")
        response = get_response(request)
        # post processing
        print("pre-processing message")
        return response
    
    return middleware
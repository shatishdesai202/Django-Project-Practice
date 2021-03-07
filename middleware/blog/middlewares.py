from django.shortcuts import HttpResponse

def my_middleware(get_response):
    print('one time initializations')

    def my_function(request):
        print('this is before view')
        response = get_response(request)
        print('this is after view')
        return response
    return my_function


class my_father:
    def __init__(self, get_response):
        self.get_response = get_response
        print('CLASS BASE MIDDLEWARE --> first-time-initialization father')

    def __call__(self, request):
        print('This is before view father')
        response = self.get_response(request)
        print('This is after view father')

        return response


class my_mother:
    def __init__(self, get_response):
        self.get_response = get_response
        print('CLASS BASE MIDDLEWARE --> first-time-initialization mother')

    def __call__(self, request):
        print('This is before view mother')
        response = self.get_response(request)
        print('This is after view mother')
        return response


class my_brother:
    def __init__(self, get_response):
        self.get_response = get_response
        print('CLASS BASE MIDDLEWARE --> first-time-initialization brother')

    def __call__(self, request):
        print('This is before view brother')
        response = self.get_response(request)
        print('This is after view brother')
        return response

    def process_view(self, request, *args, **kwargs):
        print('process view')

    def process_exception(self, request, exception):
        msg = exception
        print('Exception', msg)
        return HttpResponse('middleware exception')
    
    def process_template_response(self, request, response):
        print('template respose')
        response.context_data['name'] = 'babu'
        return response


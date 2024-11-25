from django.shortcuts import redirect


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser and request.path in ['/signin/', '/signup/', '/admin/']:
            return redirect('welcome')
        response = self.get_response(request)
        return response

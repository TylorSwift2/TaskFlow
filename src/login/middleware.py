from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    """
    Middleware that ensures the user is authenticated before accessing certain pages.
    If the user is not authenticated and tries to access a protected route,
    they are redirected to the login page.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware with the next response handler.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Checks if the user is authenticated. If not, and the requested path is not
        in the list of allowed paths (LOGIN_URL, RE, HOME), redirects to the login page.
        """
        print(f"Middleware called for: {request.path}")
        print(f"User authenticated? {request.user.is_authenticated}")

        # Check if the user is not authenticated and is trying to access a protected route
        if not request.user.is_authenticated and request.path not in [settings.LOGIN_URL, settings.RE, settings.HOME]:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin-dashboard/') and not request.user.is_superuser:
            return redirect(reverse('no-permission'))  # or show 403 page
        return self.get_response(request)

from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def process_request(self, request):
        pass
        #
        # user = getattr(request, "user", None)
        # if "login" not in request.path:
        #     if (user is None) or (not user.is_authenticated()):
        #         request.path = reverse("login")
        #         request.path_info = reverse("login")
        #         HttpResponseRedirect(reverse("login"))


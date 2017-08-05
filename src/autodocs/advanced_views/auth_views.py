from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    authentication_form = AuthenticationForm

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(reverse("index"))
    else:
        form = authentication_form(request)
    context = {'form': form, 'site_name': "AutoDocs"}
    return TemplateResponse(request, "registration/login.html", context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("login"))


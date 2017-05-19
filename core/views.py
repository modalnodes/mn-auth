from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from rest_framework_jwt.settings import api_settings

from .models import *

from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout



def login(request):
	if request.method == "GET":
		return render(request, "login.html")
	else:
		u = request.POST.get("u")
		p = request.POST.get("p")
		user = authenticate(username=u, password=p)
		if user is not None:
			do_login(request, user)
			return HttpResponseRedirect("/")
		else:
			return render(request, "login.html", {"error":"Username o pw sbagliate"})

def logout(request):
	do_logout(request)
	return HttpResponseRedirect("/")



@login_required
def dash(request):

	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

	payload = jwt_payload_handler(request.user)
	token = jwt_encode_handler(payload)

	svcs = Application.objects.filter(enabled__usr=request.user)

	if svcs.count() > 1:

		return render(request, "dashboard.html", {
			"token":token, 
			"services":svcs, 
			"len":svcs.count()})
	else:
		svc = svcs[0]
		full_url = "%s%s%s" % (svc.url, svc.urlmode, token)
		return HttpResponseRedirect(full_url)
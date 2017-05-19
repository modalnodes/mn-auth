"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core.views import * 

from rest_framework_swagger.views import get_swagger_view

import rest_framework_jwt.views

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),  # using JSON web token
    url(r'^auth/', include('djoser.urls.authtoken')),

    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^docs$', schema_view),
    url(r'^$', dash),
    

]

from django.contrib import admin

from .models import *

admin.site.register(UrlMode)
admin.site.register(Application)
admin.site.register(AppConfiguration)
admin.site.register(ClaimType)
admin.site.register(AppClaim)
admin.site.register(UserClaim)
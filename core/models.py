from __future__ import unicode_literals

import uuid
import json

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UrlMode(models.Model):
	name = models.CharField(max_length=100)
	urlpart = models.CharField(max_length=100)

	def __str__(self):
		return "{0} ({1})".format(self.name, self.urlpart)

class Application(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	logo = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField(blank=True, null=True)	
	color = models.CharField(max_length=10, blank=True, null=True)
	textcolor = models.CharField(max_length=10, blank=True, null=True)
	description = models.TextField()

	urlmode = models.ForeignKey(UrlMode)

	key = models.UUIDField(default=uuid.uuid4)

	img = models.TextField()

	pic = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class AppConfiguration(models.Model):
	usr = models.ForeignKey(User)
	application = models.ForeignKey(Application, related_name="enabled")

	conf = models.TextField()

DATA_TYPES = (
    ('int', 'Integer'),
    ('str', 'String'),
    ('json', 'JSON Object'),
    ('array|int', 'Array of integer'),
    ('array|str', 'Array of string'),
)

class ClaimType(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=100, choices=DATA_TYPES)
	
	def __unicode__(self):
		return self.name
	
class AppClaim(models.Model):
	application = models.ForeignKey(Application, related_name="valid_claims")
	claim = models.ForeignKey(ClaimType)

class UserClaim(models.Model):
	user = models.ForeignKey(User, related_name="claims")
	claim = models.ForeignKey(ClaimType)
	value = models.TextField()

# --- API

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	app_permissions = serializers.SerializerMethodField()

	def get_app_permissions(self, obj):
		k = self.context['request'].GET.get("app")
		if k:
			k = str(uuid.UUID(k))
			print k
			c = ConfApplicativo.objects.filter(usr=obj, applicativo__key=k)
			print c
			if (c.count() == 1):
				return json.loads(c[0].conf)
		else:
			return None

	class Meta:
		model = User
		fields = ["username","first_name","last_name", "email", "app_permissions"]
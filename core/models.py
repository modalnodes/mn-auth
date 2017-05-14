from __future__ import unicode_literals

import uuid
import json

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	logo = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField(blank=True, null=True)	
	color = models.CharField(max_length=10, blank=True, null=True)
	textcolor = models.CharField(max_length=10, blank=True, null=True)
	description = models.TextField()

	key = models.UUIDField(default=uuid.uuid4)

	img = models.TextField()

	pic = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class AppConfiguration(models.Model):
	usr = models.ForeignKey(User)
	applicativo = models.ForeignKey(Application, related_name="enabled")

	conf = models.TextField()

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
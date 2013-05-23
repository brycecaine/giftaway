from django.contrib.auth.models import User
from django.db import models

class Occasion(models.Model):
	description = models.CharField(max_length=255)
	month = models.CharField(max_length=12)
	day = models.IntegerField(blank=True, null=True)
	rule = models.CharField(max_length=80, blank=True, null=True)

class Gift(models.Model):
	giver = models.ForeignKey(User, related_name='gift_givers')
	recipient = models.ForeignKey(User, related_name='gift_recipients')
	occasion = models.ForeignKey(Occasion, blank=True, null=True)
	occasion_date = models.DateField(blank=True, null=True)
	order_date = models.DateField(blank=True, null=True)
	delivery_date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=255)
	merchant = models.CharField(max_length=80, blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	tracking_number = models.CharField(max_length=255, blank=True, null=True)
	cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
	recipient_liked = models.IntegerField(blank=True, null=True)

class Idea(models.Model):
	giver = models.ForeignKey(User, related_name='idea_givers')
	recipient = models.ForeignKey(User, related_name='idea_recipients')
	occasion = models.ForeignKey(Occasion, blank=True, null=True)
	occasion_date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=255)

class Person(User):
	birthday = models.DateField(blank=True, null=True)
	interests = models.CharField(max_length=1000, blank=True, null=True)
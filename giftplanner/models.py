from django.contrib.auth.models import User
from django.db import models

class Occasion(models.Model):
	description = models.CharField(max_length=255)
	month = models.CharField(max_length=12)
	day = models.IntegerField()
	rule = models.CharField(max_length=80)

class Gift(models.Model):
	giver = models.ForeignKey(User)
	recipient = models.ForeignKey(User)
	occasion = models.ForeignKey(Occasion)
	occasion_date = models.DateField()
	order_date = models.DateField()
	delivery_date = models.DateField()
	description = models.CharField(max_length=255)
	merchant = models.CharField(max_length=80)
	url = models.URLField()
	tracking_number = models.CharField(max_length=255)
	cost = models.DecimalField(max_digits=20, decimal_places=2)
	recipient_liked = models.IntegerField()

class Idea(models.Model):
	giver = models.ForeignKey(User)
	recipient = models.ForeignKey(User)
	occasion = models.ForeignKey(Occasion)
	occasion_date = models.DateField()
	gift = models.ForeignKey(Gift)

class Person(User):
	birthday = models.DateField()
	interests = models.CharField(max_length=1000)
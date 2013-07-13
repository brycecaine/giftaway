from django.contrib.auth.models import User
from django.db import models

class Holiday(models.Model):
	name = models.CharField(max_length=255)
	month = models.IntegerField()
	day = models.IntegerField(blank=True, null=True)
	weekday = models.IntegerField(blank=True, null=True)
	ordinal = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return '{0}'.format(self.name)

class Occasion(models.Model):
	giver = models.ForeignKey(User, related_name='occasion_givers')
	recipient = models.ForeignKey(User, related_name='occasion_recipients')
	event = models.CharField(max_length=255)
	event_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return '{0}\'s {1} ({2})'.format(self.recipient, self.event, self.giver)

class Gift(models.Model):
	giver = models.ForeignKey(User, related_name='gift_givers')
	recipient = models.ForeignKey(User, related_name='gift_recipients')
	occasion = models.ForeignKey(Occasion, blank=True, null=True)
	occasion_date = models.DateField(blank=True, null=True)
	name = models.CharField(max_length=255)
	idea = models.BooleanField()
	purchase_date = models.DateField(blank=True, null=True)
	delivery_date = models.DateField(blank=True, null=True)
	merchant = models.CharField(max_length=80, blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	tracking_number = models.CharField(max_length=255, blank=True, null=True)
	cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
	recipient_liked = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return '{0} (to {1} from {2})'.format(self.name, self.giver, self.recipient)

class Interest(User):
	giver = models.ForeignKey(User, related_name='interest_givers')
	recipient = models.ForeignKey(User, related_name='interest_recipients')
	name = models.CharField(max_length=255)
	interest_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return '{0}: {1} ({2})'.format(self.recipient, self.name, self.giver)

# So a user can choose what holidays show up in their opportunity list
class GiverHoliday(models.Model):
	giver = models.ForeignKey(User)
	holiday = models.ForeignKey(Holiday)

from tastypie.resources import ModelResource
from giftplanner.models import Gift

class GiftResource(ModelResource):
    class Meta:
        queryset = Gift.objects.all()
        resource_name = 'gift'
from tastypie.resources import ModelResource
from giftplanner.models import Gift, Occasion, Idea, Person

class GiftResource(ModelResource):
    class Meta:
        queryset = Gift.objects.all()
        resource_name = 'gift'

class OccasionResource(ModelResource):
    class Meta:
        queryset = Occasion.objects.all()
        resource_name = 'occasion'

class IdeaResource(ModelResource):
    class Meta:
        queryset = Idea.objects.all()
        resource_name = 'idea'

class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
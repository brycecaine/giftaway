from tastypie.resources import ModelResource
from giftplanner.models import Holiday, Occasion, Gift, Interest, GiverHoliday

class HolidayResource(ModelResource):
    class Meta:
        queryset = Holiday.objects.all()
        resource_name = 'holiday'

class OccasionResource(ModelResource):
    class Meta:
        queryset = Occasion.objects.all()
        resource_name = 'occasion'

class GiftResource(ModelResource):
    class Meta:
        queryset = Gift.objects.all()
        resource_name = 'gift'

class InterestResource(ModelResource):
    class Meta:
        queryset = Interest.objects.all()
        resource_name = 'interest'

class GiverHolidayResource(ModelResource):
    class Meta:
        queryset = GiverHoliday.objects.all()
        resource_name = 'giverholiday'
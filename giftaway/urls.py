from django.conf.urls import patterns, include, url
from giftplanner.api import HolidayResource, OccasionResource, GiftResource, InterestResource, GiverHolidayResource
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

holiday_resource = HolidayResource()
occasion_resource = OccasionResource()
gift_resource = GiftResource()
interest_resource = InterestResource()
giverholiday_resource = GiverHolidayResource()

urlpatterns = patterns('',
    url(r'^$', 'giftplanner.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',name='my_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name='my_logout'),
    # url(r'^giftplanner/', include('giftplanner.urls')),
    # Examples:
    # url(r'^$', 'giftaway.views.home', name='home'),
    # url(r'^giftaway/', include('giftaway.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(holiday_resource.urls)),
    (r'^api/', include(occasion_resource.urls)),
    (r'^api/', include(gift_resource.urls)),
    (r'^api/', include(interest_resource.urls)),
    (r'^api/', include(giverholiday_resource.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

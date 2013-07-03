from django.conf.urls import patterns, include, url
from giftplanner.api import GiftResource, OccasionResource, IdeaResource, PersonResource
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

gift_resource = GiftResource()
occasion_resource = OccasionResource()
idea_resource = IdeaResource()
person_resource = PersonResource()

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
    (r'^api/', include(gift_resource.urls)),
    (r'^api/', include(occasion_resource.urls)),
    (r'^api/', include(idea_resource.urls)),
    (r'^api/', include(person_resource.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

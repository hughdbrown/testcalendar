from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('testcalendar.views',
    url(r'^admin/(.*)',     admin.site.root),
    url(regex=r'^gencal/$', view="foo", kwargs=None, name="foo"),
    url(regex=r'^simple-gencal/$', view="bar", kwargs=None, name="bar"),
    url(regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$', view='index', kwargs=None, name='gencal'),
    url(regex=r'^event/(?P<object_id>\d+)/$', view="event", kwargs=None, name="event"),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('testcalendar.views',
	url(regex=r'^gencal/$', view="foo", kwargs=None, name="foo"),
	url(regex=r'^simple-gencal/$', view="bar", kwargs=None, name="bar"),
	url(regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$', view='index', kwargs=None, name='gencal'),
)

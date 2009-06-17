from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(regex=r'^gencal/$', view="testcalendar.views.foo", kwargs=None, name="foo"),
	url(regex=r'^simple-gencal/$', view="testcalendar.views.bar", kwargs=None, name="bar"),
	url(regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$', view='testcalendar.views.index', kwargs=None, name='gencal'),
)

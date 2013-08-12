from django.conf.urls.defaults import include, patterns

# Do this so that the mozilla_extras.urls's urlpatterns comes first
from mozilla_extras.urls import urlpatterns
from pootle.urls import urlpatterns as pootle_urlpatterns
urlpatterns += pootle_urlpatterns

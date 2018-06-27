from django.conf.urls import url, include
from rest_framework import routers
from igwcoeffs.views import *


urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^igwcoeffs/', igwcoeffs, name='igwcoeffs'),
    url(r'^igwcoeffs_about/', igwcoeffs_about, name='igwcoeffs_about')
]

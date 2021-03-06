# -*- coding: utf-8 -*-

from django.conf.urls import *
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^currencies/', include('currencies.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)

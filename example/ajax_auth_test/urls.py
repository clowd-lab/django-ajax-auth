__author__ = 'amenon'

from django.conf.urls import *

from ajax_auth_test import views

urlpatterns = patterns('',
                       url(r'^$', views.HomePageView.as_view()),
)

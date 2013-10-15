from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^ajax_auth/', include('ajax_auth.urls')),
                       url(r'^', include('ajax_auth_test.urls')),
)

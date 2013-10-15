from django.views.generic import TemplateView

__author__ = 'amenon'

class HomePageView(TemplateView):
    template_name = "ajax_auth_test/index.html"
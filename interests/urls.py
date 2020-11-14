from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from interests import views

urlpatterns = [
    url(r'^api/get-interest/$', views.GetInterest.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
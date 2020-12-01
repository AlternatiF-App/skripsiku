from django.urls import path, re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from students import views

urlpatterns = [
    url(r'^api/update-clusters/$', views.UpdateCluster.as_view()),
    path('api/clusters/', views.GetClusters.as_view()),
    path('api/students/', views.StudentList.as_view()),
    path('api/students-update/', views.StudentsUpdateClusterList.as_view()),
    path('api/students/<int:pk>/', views.StudentDetail.as_view()),
    re_path('^api/students/(?P<teacher>.+)/$', views.StudentsListByUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
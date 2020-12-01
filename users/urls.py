from django.urls import path
from .views import *

urlpatterns = [
    path('api/getuser/', GetUserView.as_view(), name="get"),
    path('api/detail-user/<int:pk>/', UsersDetail.as_view(), name="detail"),
    path('api/getuser/<int:pk>/', UserUpdate.as_view(), name="detail"),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/login/', LoginAPIView.as_view(), name="login"),
    path('api/logout/', LogoutAPIView.as_view(), name="logout"),
]

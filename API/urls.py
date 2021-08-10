from django.urls import path
from .views import *

urlpatterns = [
    
    path('', JobList.as_view(), name='list_view'),
    path('users/', UserDetails.as_view(), name='users'),
    path('<uuid:id>/', JobDetail.as_view(), name='detail_view'),
]
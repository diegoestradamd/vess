from django.urls import path 
from.views import HealthCareUserCreateView

urlpatterns = [
    path('signup/', HealthCareUserCreateView.as_view(), name='signup'),
]
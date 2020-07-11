from django.urls import path
from testseriesapp.views import HomePageView,join_test_series_method
app_name = 'testseriesapp'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('join/<int:id>',join_test_series_method,name='join-now'),
]
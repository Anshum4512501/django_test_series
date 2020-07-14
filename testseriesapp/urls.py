from django.urls import path
from testseriesapp.views import HomePageView,join_test_series_method,TestDetailView,QuestionListView,update_choices,TestResultDetailView
app_name = 'testseriesapp'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('join/<int:id>',join_test_series_method,name='join-now'),
    path('testseries/<slug:pk>/details',TestDetailView.as_view(),name='test-series-details'),
    path('question-list',QuestionListView.as_view(),name='question-list'),
    path('update-choice/',update_choices,name='update-choices'),
    path('testresult/<int:pk>',TestResultDetailView.as_view(),name='test-result'),
]
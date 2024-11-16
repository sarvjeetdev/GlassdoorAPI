# urls.py
from django.urls import path
from .views import GlassdoorJobsListCreateView

urlpatterns = [
    path('jobs/', GlassdoorJobsListCreateView.as_view(), name='glassdoor-jobs-list-create'),
]

# views.py
from rest_framework import generics
from .models import GlassdoorJobs
from .serializers import GlassdoorJobsSerializer

# GET request to list jobs, POST request to add a new job
class GlassdoorJobsListCreateView(generics.ListCreateAPIView):
    queryset = GlassdoorJobs.objects.all()
    serializer_class = GlassdoorJobsSerializer

# serializers.py
from rest_framework import serializers
from .models import GlassdoorJobs

class GlassdoorJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlassdoorJobs
        fields = '__all__'

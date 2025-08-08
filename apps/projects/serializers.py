from rest_framework import serializers
from apps.projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # TODO: The employer model and its relationships need to be specified later
    employer_name = serializers.CharField(source='employer.username', read_only=True) 

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'code', 'description', 'employer', 'employer_name',
            'start_date', 'end_date', 'progress', 'status', 'lat', 'lng',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
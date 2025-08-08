from rest_framework import viewsets
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD for projects.

    - Lists all projects with their employers.
    - Search by name, code, description, employer.
    - Order by creation date, start/end date, progress.
    - Sets current user as employer if not given on create.
    """
    queryset = Project.objects.all().select_related('employer')
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated] # Uncomment if you want to restrict access to authenticated users
    search_fields = ['name', 'code', 'description', 'employer__username']
    ordering_fields = ['created_at', 'start_date', 'end_date', 'progress']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        # اگر employer ارسال نشد، کاربر جاری رو قرار بده
        if not serializer.validated_data.get('employer'):
            serializer.save(employer=self.request.user)
        else:
            serializer.save()
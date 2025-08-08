from django.contrib import admin
from apps.projects.models import Project, Phase, Activity, Dependency

admin.site.register(Project)
admin.site.register(Phase)  
admin.site.register(Activity)
admin.site.register(Dependency)
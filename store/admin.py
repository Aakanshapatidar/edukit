from django.contrib import admin
from .models import Course, RoadmapStep, UserProgress

admin.site.register(Course)
admin.site.register(RoadmapStep)
admin.site.register(UserProgress)

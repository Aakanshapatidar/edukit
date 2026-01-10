from django.db import models
from django.contrib.auth.models import User


# --------------------
# Course Model
# --------------------
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# --------------------
# Roadmap Step Model
# --------------------
class RoadmapStep(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.course.name} - Step {self.order}: {self.title}"


# --------------------
# User Progress Model
# --------------------
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.step.title}"

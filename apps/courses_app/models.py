from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def validator(self,data):
        errors = {}
        if len(data["name"]) < 6:
            errors["name"] = "Course name has to be longer than 5 characters"
        if len(data["description"]) < 16:
            errors["description"] = "Course description has to be longer than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


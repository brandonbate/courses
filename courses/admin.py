from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from courses import models

admin.site.register(models.User, UserAdmin)

admin.site.register(models.Course)
admin.site.register(models.Term)
admin.site.register(models.CourseInstance)
admin.site.register(models.CourseInstanceInstructor)
admin.site.register(models.CourseInstanceStudent)

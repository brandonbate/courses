from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from courses.models import Course, Term, CourseInstance, User

admin.site.register(Course)
admin.site.register(Term)
admin.site.register(CourseInstance)
admin.site.register(User, UserAdmin)
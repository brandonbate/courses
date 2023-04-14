from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from courses import models

admin.site.register(models.User, UserAdmin)

#admin.site.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'number', 'title', 'credit_hours')
    list_filter = ('prefix',)

admin.site.register(models.Course, CourseAdmin)

admin.site.register(models.Term)

# This decorator essentially calls
# admin.site.register(models.CourseInstance, CourseInstanceAdmin)
@admin.register(models.CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'number', 'section', 'title', 'term', 'instructor')

    def prefix(self, obj):
        return obj.course.prefix

    def number(self, obj):
        return obj.course.number

    def title(self, obj):
        return obj.course.title

    def instructor(self, obj):
        return ", ".join(str(x.instructor) for x in models.CourseInstanceInstructor.objects.filter(course_instance=obj))

admin.site.register(models.CourseInstanceInstructor)
admin.site.register(models.CourseInstanceStudent)

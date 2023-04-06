from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView

from courses.models import Course

# Create your views here.
def index(request):
    return render(request, 'index.html')

class CourseCatalogListView(LoginRequiredMixin, ListView):
    model = Course
    
class CreateCourseFormView(PermissionRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    permission_required = 'courses.course_add'
    success_url = '/'
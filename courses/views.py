from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from courses.models import Course

# Create your views here.
def index(request):
    return render(request, 'index.html')

class CourseCatalogListView(LoginRequiredMixin, ListView):
    model = Course
    
class CreateCourseFormView(LoginRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    success_url = '/'
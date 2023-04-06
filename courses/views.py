from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('catalog')
    
class UpdateCourseFormView(PermissionRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    permission_required = 'courses.course_change'
    success_url = reverse_lazy('catalog')

class DeleteCourseFormView(PermissionRequiredMixin, DeleteView):
    model = Course
    permission_required = 'courses.course_delete'
    success_url = reverse_lazy('catalog')

class DetailCourseFormView(DetailView):
    model = Course

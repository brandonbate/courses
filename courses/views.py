from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from courses.models import Course, Term


def index(request):
    return render(request, 'index.html')

# Course Views

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    
class CourseCreateFormView(PermissionRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    permission_required = 'courses.course_add'
    success_url = reverse_lazy('course_list')
    
class CourseUpdateFormView(PermissionRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    permission_required = 'courses.course_change'
    success_url = reverse_lazy('course_list')

class CourseDeleteFormView(PermissionRequiredMixin, DeleteView):
    model = Course
    permission_required = 'courses.course_delete'
    success_url = reverse_lazy('course_list')

class CourseDetailFormView(DetailView):
    model = Course

# Term Views

class TermListView(LoginRequiredMixin, ListView):
    model = Term
    
class TermCreateFormView(PermissionRequiredMixin, CreateView):
    model = Term
    fields = '__all__'
    permission_required = 'courses.term_add'
    success_url = reverse_lazy('term_list')
    
class TermUpdateFormView(PermissionRequiredMixin, UpdateView):
    model = Term
    fields = '__all__'
    permission_required = 'courses.term_change'
    success_url = reverse_lazy('term_list')

class TermDeleteFormView(PermissionRequiredMixin, DeleteView):
    model = Term
    permission_required = 'courses.term_delete'
    success_url = reverse_lazy('term_list')

class TermDetailFormView(DetailView):
    model = Term


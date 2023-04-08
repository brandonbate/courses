from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError

from courses.models import Course, Term, CourseInstance


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

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error = 'Cannot delete because there is a course instance linked to this course.'
            return render(request, 'error.html', {'error': error})


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
    
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error = 'Cannot delete because there is a course instance with this academic term.'
            return render(request, 'error.html', {'error': error})

class TermDetailFormView(DetailView):
    model = Term

# CourseInstance Views

class CourseInstanceListView(LoginRequiredMixin, ListView):
    model = CourseInstance
    
class CourseInstanceCreateFormView(PermissionRequiredMixin, CreateView):
    model = CourseInstance
    fields = '__all__'
    permission_required = 'courses.courseinstance_add'
    success_url = reverse_lazy('courseinstance_list')
    
class CourseInstanceUpdateFormView(PermissionRequiredMixin, UpdateView):
    model = CourseInstance
    fields = '__all__'
    permission_required = 'courses.courseinstance_change'
    success_url = reverse_lazy('courseinstance_list')

class CourseInstanceDeleteFormView(PermissionRequiredMixin, DeleteView):
    model = CourseInstance
    permission_required = 'courses.courseinstance_delete'
    success_url = reverse_lazy('courseinstance_list')

class CourseInstanceDetailFormView(DetailView):
    model = CourseInstance
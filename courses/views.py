from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError

# I forgot to import these on an earlier commit!
from django.http import HttpResponseRedirect
from django.urls import reverse

from courses.models import Course, Term, CourseInstance, CourseInstanceStudent, CourseInstanceInstructor


def index(request):
    return render(request, 'index.html')

def course_instances_by_term(request):
    terms = Term.objects.all().order_by('-start_date')
    return render(request, 'course_instances_by_term.html', {'terms': terms})    

def ajax_course_instances_by_term(request):
    term_id = request.GET.get('term')
    course_instances = CourseInstance.objects.filter(term = term_id)
    print(course_instances)
    for ci in course_instances:
        ci.instructors = '; '.join([str(x.instructor) for x in CourseInstanceInstructor.objects.filter(course_instance = ci)])
        
    return render(request,
                  'ajax_course_instances_by_term.html',
                  {'course_instances': course_instances})

def enroll_in_course(request, pk):
    user = request.user
    
    if not user.is_authenticated:
        error = 'Must be logged in to enroll in a course.'
        return render(request, 'error.html', {'error': error})
    
    course_instance = CourseInstance.objects.get(id = pk)
    
    if not course_instance:
        error = 'Must be logged in to enroll in a course.'
        return render(request, 'error.html', {'error': error})

    new_enrollment = CourseInstanceStudent(course_instance = course_instance, student=user)
    new_enrollment.save()

    return HttpResponseRedirect(reverse('courseinstance_detail', kwargs={'pk':course_instance.id}))

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
    
    def get_context_data(self, **kwargs):
        context = super(CourseInstanceDetailFormView, self).get_context_data(**kwargs)
        context['students'] = [x.student for x in CourseInstanceStudent.objects.filter(course_instance = self.object)]
        context['instructors'] = [x.instructor for x in CourseInstanceInstructor.objects.filter(course_instance = self.object)]

        return context
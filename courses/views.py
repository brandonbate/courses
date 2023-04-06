from django.shortcuts import render
from django.views import generic
from courses.models import Course

# Create your views here.
def index(request):
    return render(request, 'index.html')

class CourseCatalogListView(generic.ListView):
    model = Course
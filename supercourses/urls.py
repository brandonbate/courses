"""
URL configuration for supercourses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from courses import views

urlpatterns = [
    path('', views.index, name='index'),

    path('course-instances-by-term/', views.course_instances_by_term, name='course_instances_by_term'),
    path('ajax/course-instances-by-term/', views.ajax_course_instances_by_term, name='ajax_course_instances_by_term'),
    
    path('course/list/', views.CourseListView.as_view(), name='course_list'),
    path('course/create/', views.CourseCreateFormView.as_view(), name='course_create'),
    path('course/<int:pk>/update/', views.CourseUpdateFormView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDeleteFormView.as_view(), name='course_delete'),
    path('course/<int:pk>/detail/', views.CourseDetailFormView.as_view(), name='course_detail'),

    path('term/list/', views.TermListView.as_view(), name='term_list'),
    path('term/create/', views.TermCreateFormView.as_view(), name='term_create'),
    path('term/<int:pk>/update/', views.TermUpdateFormView.as_view(), name='term_update'),
    path('term/<int:pk>/delete/', views.TermDeleteFormView.as_view(), name='term_delete'),
    path('term/<int:pk>/detail/', views.TermDetailFormView.as_view(), name='term_detail'),

    path('courseinstance/list/', views.CourseInstanceListView.as_view(), name='courseinstance_list'),
    path('courseinstance/create/', views.CourseInstanceCreateFormView.as_view(), name='courseinstance_create'),
    path('courseinstance/<int:pk>/update/', views.CourseInstanceUpdateFormView.as_view(), name='courseinstance_update'),
    path('courseinstance/<int:pk>/delete/', views.CourseInstanceDeleteFormView.as_view(), name='courseinstance_delete'),
    path('courseinstance/<int:pk>/detail/', views.CourseInstanceDetailFormView.as_view(), name='courseinstance_detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

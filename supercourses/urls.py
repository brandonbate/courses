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
    
    path('course/list/', views.CourseListView.as_view(), name='course_list'),
    path('course/create', views.CourseCreateFormView.as_view(), name='course_create'),
    path('course/<int:pk>/update/', views.CourseUpdateFormView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', views.CourseDeleteFormView.as_view(), name='course_delete'),
    path('course/<int:pk>/detail/', views.CourseDetailFormView.as_view(), name='course_detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

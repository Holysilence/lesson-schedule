
from django.contrib import admin
from django.urls import path

from lessons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('lessons/<int:student_id>/', views.student_detail, name='student_detail')
]

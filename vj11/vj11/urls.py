from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>/', views.student_api),
]

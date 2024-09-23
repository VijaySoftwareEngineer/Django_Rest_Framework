from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/<int:pk>/', views.StudentRetriveUpdateDestroy.as_view()),
    path('studentapi/', views.StudentListCreate.as_view()),
]

from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetriveUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetriveDestroy.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetriveUpdateDestroy.as_view()),

    path('studentapi/', views.StudentListCreate.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('updatestudent/<id>', views.updatestudent, name='updatestudent'),
    path('editstudent/<id>/', views.edit_student, name='edit_store'),
    path('add_student/', views.add_student, name='addstore'),
    path('deletestore/<id>/', views.delete_store, name='delete_store'),
    path('stores/', views.stores, name='store'),
]
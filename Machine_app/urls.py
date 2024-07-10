from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.machine_list, name='machine_list'),
    path('machines/create/', views.machine_create, name='machine_create'),
    path('machines/<int:pk>/edit/', views.machine_update, name='machine_update'),
    path('machines/<int:pk>/delete/', views.machine_delete, name='machine_delete'),
    path('machines/<int:pk>/', views.machine_detail, name='machine_detail'),
]

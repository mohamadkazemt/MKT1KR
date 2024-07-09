from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.machine_list, name='machine_list'),
    path('machine/<int:pk>/', views.machine_detail, name='machine_detail'),
    path('machine/new/', views.machine_create, name='machine_create'),
    path('machine/<int:pk>/edit/', views.machine_update, name='machine_update'),
    path('machine/<int:pk>/delete/', views.machine_delete, name='machine_delete'),
]

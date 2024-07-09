from django.urls import path
from . import views

urlpatterns = [
    path('operators/', views.operator_list, name='operator_list'),
    path('operator/<int:pk>/', views.operator_detail, name='operator_detail'),
    path('operator/new/', views.operator_create, name='operator_create'),
    path('operator/<int:pk>/edit/', views.operator_update, name='operator_update'),
    path('operator/<int:pk>/delete/', views.operator_delete, name='operator_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('operators/', views.operator_list, name='operator_list'),
    path('operators/create/', views.operator_create, name='operator_create'),
    path('operators/<int:pk>/edit/', views.operator_update, name='operator_update'),
    path('operators/<int:pk>/delete/', views.operator_delete, name='operator_delete'),
    path('operators/<int:pk>/', views.operator_detail, name='operator_detail'),
]

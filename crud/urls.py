from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/gender/list'), name='home'),
    
    # Without slash
    path('gender/list', views.gender_list, name='gender_list'),
    path('gender/add', views.add_gender, name='add_gender'),
    path('gender/edit/<int:pk>', views.edit_gender, name='edit_gender'),
    path('gender/delete/<int:pk>', views.delete_gender, name='delete_gender'),
    
    # With slash (for browser auto-redirect)
    path('gender/list/', views.gender_list),
    path('gender/add/', views.add_gender),
    path('gender/edit/<int:pk>/', views.edit_gender),
    path('gender/delete/<int:pk>/', views.delete_gender),
]
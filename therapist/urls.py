from django.urls import path
from . import views
from .views import user_list, dashboard


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/diary/', views.diary, name='diary'),
    path('userlist/', user_list, name='user_list'),
    path('dashboard/diary/add/', views.add_diary_entry, name='add_diary_entry'),
    path('Experiences/', views.Experiences, name='Experiences'),
    path('Blog/', views.Blog, name='Blog'),
    path('client/<int:client_id>/assessments/', views.assessment_list, name='assessment_list'),
    path('client/<int:client_id>/add/', views.add_assessment, name='add_assessment'),
]

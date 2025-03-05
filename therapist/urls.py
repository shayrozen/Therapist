from django.urls import path
from . import views
from .views import user_list, dashboard, intake_form, Registration, custom_login_view, intake_summary
from django.views.generic import TemplateView
from .views import dashboard_view, diary_view



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path("diary/", diary_view, name="diary"),
    path('userlist/', user_list, name='user_list'),
    path('Experiences/', views.Experiences, name='Experiences'),
    path('Blog/', views.Blog, name='Blog'),
    path('Registration/', views.Registration, name='Registration'),
    # path('client/<int:client_id>/assessments/', views.assessment_list, name='assessment_list'),
    # path('assessments/', views.assessment_list, name='assessment_list_no_client'),
    # path('client/<int:client_id>/add/', views.add_assessment, name='add_assessment'),
    # path('assessments/add/', views.add_assessment, name='add_assessment_no_client'),
    # path("intake/", views.preli
    # minary_intake, name="preliminary_intake"),
    path("intake/", intake_form, name="intake"),
    path("intake/summary/", intake_summary, name="intake_summary"),
    # path("assessment/", views.assessment_view, name="assessment"),
    # path("assessment/results/", views.assessment_results, name="assessment_results"),
    path('registration-success/', TemplateView.as_view(template_name="registration/success.html"), name='registration_success'),
    path("login/", custom_login_view, name="custom_login"),
]

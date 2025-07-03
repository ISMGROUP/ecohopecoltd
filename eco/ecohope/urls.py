from django.urls import path
from .views import search_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This ensures the root URL ('/') is handled by the home view
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('careers/', views.careers, name='careers'),
    path('careers/<int:job_id>/', views.job_detail, name='job_detail'),
     path('careers/<int:job_id>/apply/', views.apply_to_job, name='apply_to_job'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'), 
    path('contact/', views.contact, name='contact'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('search/', views.search, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('our_team/', views.our_team, name='our_team'),
    path('our_story/', views.our_story, name='our_story'),
    path('awards/', views.awards, name='awards'),
    path('clients/', views.clients, name='clients'),
    path('press/', views.press, name='press'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('consultation/', views.consultation, name='consultation'),
    path('consultation/submitted/', views.consultation_submitted, name='consultation_submitted'),
    path('search/', search_view, name='search'),
    path('crop_solutions/', views.crop_solutions, name='crop_solutions'),
    path('equipment/', views.equipment, name='equipment'),
    path('terms/', views.terms, name='terms'),
     path('contact_successiful/', views.contact_successiful, name='contact_successiful'),
    path('subscription_successiful/', views.subscription_successiful, name='subscription_successiful'),
    path('application_successiful/', views.application_successiful, name='application_successiful'),

]


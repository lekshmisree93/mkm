from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallary/', views.gallary, name='gallary'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('booking/', views.booking, name='booking'),
]
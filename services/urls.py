from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='list'),
    path('solar/', views.solar_packages, name='solar'),
    path('borehole/', views.borehole_pricing, name='borehole'),
    path('<slug:slug>/', views.service_detail, name='detail'),
]

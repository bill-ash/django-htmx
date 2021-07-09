from django.urls import path 
from . import views 

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.homeform_view, name='contact'),
]

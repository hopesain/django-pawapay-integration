from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('initialize_payment/', views.initialize_payment, name = 'initialize_payment'),
    path('process_payment/', views.process_payment, name = 'process_payment'),
]
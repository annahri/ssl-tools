from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form),
    path('generate-csr/', views.generateCSR, name='generate-csr'),
    path('decode-csr/', views.decodeCSR, name='decode-csr'),
    path('verify-ssl/', views.verifySSL, name='verify-ssl')
]

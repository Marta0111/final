# users/urls.py
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import PrivacyPolicyView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('add/', addContactView.as_view(), name='add-contact'),
    path('edit/<int:pk>/', editContactView.as_view(), name='edit-contact'),
    path('delete/<int:pk>/', DeleteContactView.as_view(), name='delete-contact'),
    path('contact/<int:pk>/', contactDetailView.as_view(), name='contact-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
]




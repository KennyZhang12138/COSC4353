# URL mappings for the application
from django.urls import path
from .views import LoginPageView, HomePageView, ProfilePageView, buyPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('profile/', ProfilePageView.as_view(), name = 'profile'),
    path('buy/', buyPage, name='buy'),
    ]
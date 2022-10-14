from django.urls import path

from .views import registroView, loginView, homeView, logoutView

urlpatterns = [
    path('registro', registroView, name='registro'),
    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),
    path('', homeView, name='home'),
]
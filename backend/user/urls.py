from django.urls import path
from user import views



urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_view'),
    
]

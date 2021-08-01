from django.urls import path
from accounts import views

# app_name = "accounts"

urlpatterns = [
    path('register-view/', views.RegisterView.as_view(), name='register-view'),
]

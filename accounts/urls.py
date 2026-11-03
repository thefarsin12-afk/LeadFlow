from django.urls import path

from accounts.views import UserRegisterView,GetMeView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    path('register/',UserRegisterView.as_view()),

    path('token/',TokenObtainPairView.as_view()),

    path('token/refresh/',TokenRefreshView.as_view()),

    path('profile/',GetMeView.as_view()),

    
]
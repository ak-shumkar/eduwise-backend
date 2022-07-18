from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('auth/accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('profiles/me/', views.MyProfileView.as_view(), name='my_profile'),
]

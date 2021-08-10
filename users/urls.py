from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('dj_rest_auth.urls')),
    # path('register/', include('dj_rest_auth.registration.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
]

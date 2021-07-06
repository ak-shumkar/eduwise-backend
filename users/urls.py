from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login')
]

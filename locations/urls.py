from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'countries/translations', views.CountryI18NViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'provinces/translations', views.ProvinceI18NViewSet)
router.register(r'provinces', views.ProvinceViewSet)
urlpatterns = router.urls

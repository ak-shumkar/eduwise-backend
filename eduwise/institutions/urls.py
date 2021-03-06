from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'institutions/translations', views.InstitutionI18NViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'institution_types', views.InstitutionTypeViewSet)
router.register(r'photos', views.PhotoViewSet)

urlpatterns = router.urls

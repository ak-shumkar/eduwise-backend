from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'institutions/translations', views.InstitutionI18NViewSet)
router.register(r'institutions', views.InstitutionViewSet)

urlpatterns = router.urls

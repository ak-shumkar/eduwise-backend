from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'terms', views.TermViewSet)
router.register(r'program_types', views.ProgramTypeViewSet)

urlpatterns = router.urls

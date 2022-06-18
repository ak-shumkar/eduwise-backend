from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'terms', views.TermViewSet)
router.register(r'fees', views.FeeViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'degrees', views.DegreeViewSet)
router.register(r'categories', views.FacultyViewSet)

urlpatterns = router.urls

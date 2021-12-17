from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'menus', views.MenuViewSet)
router.register(r'submenus', views.SubMenuViewSet)
router.register(r'posts', views.TextBlockViewSet)
urlpatterns = router.urls

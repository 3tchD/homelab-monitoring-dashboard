from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServerViewSet, MetricViewSet

router = DefaultRouter()
router.register(r'servers', ServerViewSet)
router.register(r'metrics', MetricViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, Kurashiru_ApiView

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("kurashiru/", Kurashiru_ApiView.as_view())
]
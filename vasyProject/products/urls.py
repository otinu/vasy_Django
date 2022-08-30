from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, NonModel_ApiView

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("non_model/", NonModel_ApiView.as_view())
]
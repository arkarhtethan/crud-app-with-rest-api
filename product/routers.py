from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet
router = DefaultRouter()

router.register('',ProductViewSet,base_name='product-viewset')
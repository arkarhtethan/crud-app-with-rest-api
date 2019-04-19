from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, LoginViewSet
router = DefaultRouter()

router.register('login',LoginViewSet,base_name='login-viewset')
router.register('products',ProductViewSet,base_name='product-viewset')
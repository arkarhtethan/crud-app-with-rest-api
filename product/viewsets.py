from rest_framework import viewsets
from .models import Product
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):

	model = Product

	serializer_class = serializers.ProductSerializer

	queryset = Product.objects.all()
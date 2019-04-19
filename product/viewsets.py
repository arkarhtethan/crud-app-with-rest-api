from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Product
from . import serializers
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):

	class Meta:

		model = Product

		fields = {
		'name':['icontains',],
		'description':['icontains',],
		'price':['lte','gte','iexact'],
		}


class ProductViewSet(viewsets.ModelViewSet):

	model = Product

	serializer_class = serializers.ProductSerializer

	queryset = Product.objects.all()

	permission_classes = (IsAuthenticatedOrReadOnly,)

	authentication_classes = (TokenAuthentication,)

	filterset_class = ProductFilter

class LoginViewSet(viewsets.ViewSet):

	serializer_class = AuthTokenSerializer

	def create(self, request):

		return ObtainAuthToken().post(request)
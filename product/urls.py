from django.urls import path, include
from . import views
from . import routers

app_name="product"

urlpatterns = [

	path('list/',views.ProductListView.as_view(),name='list'),
	path('<int:pk>/',views.ProductDetailView.as_view(),name='detail'),
	path('create/',views.ProductCreateView.as_view(),name='create'),
	path('update/<int:pk>/',views.ProductUpdateView.as_view(),name='update'),
	path('delete/<int:pk>/',views.ProductDeleteView.as_view(),name='delete'),
	path('api/',include(routers.router.urls)),

]
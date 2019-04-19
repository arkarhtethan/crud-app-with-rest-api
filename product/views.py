from django.shortcuts import render
from .models import Product
from django.views import generic
from django.urls import reverse, reverse_lazy

class ProductListView(generic.ListView):

	model = Product

class ProductDetailView(generic.DetailView):

	model = Product

class ProductCreateView(generic.CreateView):

	model = Product

	fields = "__all__"

	def get_success_url(self):
		return reverse("product:detail",kwargs={'pk':self.object.pk})

class ProductUpdateView(generic.UpdateView):

	model = Product

	fields = "__all__"

	def get_success_url(self):
		return reverse("product:detail",kwargs={'pk':self.object.pk})

class ProductDeleteView(generic.DeleteView):

	model = Product

	success_url = reverse_lazy("product:list")
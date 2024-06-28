from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"{name} - {phone} ({message})")
        return render(request, "catalog/contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

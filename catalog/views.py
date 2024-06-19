from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} - {phone} ({message})")
    return render(request, "contacts.html")


def product_list(request):
    product = Product.objects.all()
    context = {'object_list': product}
    return render(request, "home.html", context)

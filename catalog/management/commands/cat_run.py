import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("category.json", encoding="utf-8", errors='ignore') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open("product.json", encoding="utf-8", errors='ignore') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    {
                        "id": category["pk"],
                        "category_name": category["fields"]["category_name"],
                        "category_description": category["fields"]["category_description"],
                    }
                )
            )
        print(category_for_create)
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    {
                        "id": product["pk"],
                        "product_name": product["fields"]["product_name"],
                        "product_description": product["fields"]["product_description"],
                        "product_picture": product["fields"]["product_picture"],
                        "product_category": Category.objects.get(
                            pk=product["fields"]["product_category"]
                        ),
                        "price": product["fields"]["price"],
                        "created_at": product["fields"]["created_at"],
                        "updated_at": product["fields"]["updated_at"],
                    }
                )
            )

        Product.objects.bulk_create(product_for_create)

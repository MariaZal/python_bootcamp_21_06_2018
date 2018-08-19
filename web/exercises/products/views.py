from django.shortcuts import render
from products.models import Product

# Create your views here.
def product_list_view(request):
    products = Product.objects.all()
    return render(
        template_name="product_list.html",
        context={
            'products': products
        },
        request=request
    )

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(
        template_name="product_details.html",
        context={'product': product},
        request=request
    )
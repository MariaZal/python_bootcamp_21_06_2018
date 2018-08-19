from django.http import HttpResponse
from django.shortcuts import render
from example.models import Example
from products.models import Product

# Create your views here.

def hello_view(request):
    return HttpResponse(content="Hello World")
def hello_name(request,name):
    return HttpResponse(content=f'hello {name}')

def action_add(request, x, y):
   return HttpResponse(content=f'{x}+{y}={x+y}')

def action_sub(request, x, y):
   return HttpResponse(content=f'{x}-{y}={x-y}')


def examples_list_view(request):
    examples = Example.objects.all()
    return render(
        template_name="examples_list.html",
        context={
            'a': 'to jest zawartość a',
            'examples': examples
        },
        request=request
    )


def example_details(request, example_id):
    example = Example.objects.get(pk=example_id)
    return render(
        template_name="example_details.html",
        context={'example': example},
        request=request
    )



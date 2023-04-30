from django.shortcuts import render, redirect
from phones.models import Phone


def forming(phones_objects):
    phones = []
    for phone in phones_objects:
        phone_dict = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug
        }
        phones.append(phone_dict)
    return phones


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    context = {
        'phones': forming(phones_objects)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_objects = Phone.objects.filter(slug=slug)
    context = {
        'phone': forming(phones_objects)[0]
    }
    return render(request, template, context)


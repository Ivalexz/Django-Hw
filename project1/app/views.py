from django.contrib.gis.geos.libgeos import CONTEXT_PTR
from django.http import HttpResponse
from django.shortcuts import render

from project1.app.forms import CarSearchForm

cars = {
    1: {
        "Марка": "VW",
        "Модель": "Passat b5",
        "Рік": 2007,
        "Ціна": 5000
    },
    2: {
        "Марка": "VW",
        "Модель": "Golf 5",
        "Рік": 2012,
        "Ціна": 7000
    },
    3: {
        "Марка": "Audi",
        "Модель": "A4",
        "Рік": 2012,
        "Ціна": 12000
    }
}

def show_car_by_id(request, car_id):
    try:
        context={
            'car_id':car_id,
            'car':cars[car_id]
        }
    except KeyError:
        context = {'car_id': car_id, 'car': None}

    return render(request, 'app/car_details.html', context)

def search_cars(request):
    filtered_cars = []

    form = CarSearchForm(request.GET or None)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price', 0) or 0
        max_price = form.cleaned_data.get('max_price') or float('inf')
        min_year=form.cleaned_data.get('min_year', 0) or 1900
        max_year=form.cleaned_data.get("max_year") or 2025
        model=form.cleaned_data.get('model') or ""
        mark=form.cleaned_data.get('mark') or ""

        for car_id, car in cars.items():
            if min_price <= car["Ціна"] <= max_price and min_year<=car["Рік"]<=max_year and model.lower() in car["Модель"].lower() and mark.lower() in car["Марка"].lower():
                filtered_cars.append(car)

    context = {
        'filtered_cars': filtered_cars,
        'form': form
    }
    return render(request, 'app/search_cars.html', context)


def hello_world(request):
    # return HttpResponse("Hello world of Web Development!")
    return render(request, 'app/index.html')

def show_info(request):
    context={
        'cars':cars
    }
    return render(request, 'app/car_list.html', context)

def say_hello(request, name):
    return HttpResponse(f"Hello, {name}")


def greeting(request):
    return HttpResponse("Вітаємо на нашому сайті!")
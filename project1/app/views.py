from django.contrib.gis.geos.libgeos import CONTEXT_PTR
from django.http import HttpResponse
from django.shortcuts import render

from project1.app.forms import CarSearchForm, AddCarForm, DeleteCarForm, UpdateCarForm

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

def add_car(request):
    form=AddCarForm(request.POST or None)

    if form.is_valid():
        brand=form.cleaned_data.get('brand')
        model = form.cleaned_data.get('model')
        year = form.cleaned_data.get('year')
        price = form.cleaned_data.get('price')

        next_id = max(cars.keys()) + 1
        cars[next_id]={
            "Марка": brand,
            "Модель": model,
            "Рік": year,
            "Ціна": price
        }

    context={
        "form":form
    }

    return  render(request, "app/add_car.html", context)

def delete_car(request):
    form=DeleteCarForm(request.POST or None)
    if form.is_valid():
        ID=form.cleaned_data.get('ID')
        if ID in cars.keys():
            cars.pop(ID)
        else:
            return HttpResponse("Такого ID неіснує")

    context = {
        "form": form
    }

    return render(request, "app/delete_car.html", context)

def update_car(request, ID=None):
    form=UpdateCarForm(request.POST or None)

    if form.is_valid():
        brand=form.cleaned_data.get('brand') or None
        model = form.cleaned_data.get('model') or None
        year = form.cleaned_data.get('year') or None
        price = form.cleaned_data.get('price') or None

        fields_arr = {
            "Марка": brand,
            "Модель": model,
            "Рік": year,
            "Ціна": price
        }
        if ID:
            for k in cars[ID].keys():
                if fields_arr[k] is not None:
                    cars[ID][k] = fields_arr[k]

    context={
        "form":form
    }

    return render(request, "app/update_car.html", context)

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
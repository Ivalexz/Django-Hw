from django.contrib.gis.geos.libgeos import CONTEXT_PTR
from django.http import HttpResponse
from django.shortcuts import render

cars = {
    1: {
        "Марка": "VW",
        "Модель": "Passat b5",
        "Рік": "2007",
        "Ціна": 5000
    },
    2: {
        "Марка": "VW",
        "Модель": "Golf 5",
        "Рік": "2012",
        "Ціна": 7000
    },
    3: {
        "Марка": "Audi",
        "Модель": "A4",
        "Рік": "2012",
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
    min_price = request.GET.get("min_price", "0")
    max_price = request.GET.get("max_price", "999999")

    filtered_cars = []

    try:
        min_price = int(min_price)
        max_price = int(max_price)
        for car_id, car in cars.items():
            if min_price <= car["Ціна"] <= max_price:
                filtered_cars.append(car)
    except ValueError:
        pass

    context={
        'min_price':min_price,
        'max_price': max_price,
        'filtered_cars': filtered_cars
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
from django.http import HttpResponse
from django.shortcuts import render

cars = {
    1: {
        "Марка": "VW",
        "Модель": "Passat b5",
        "Рік": "2007",
        "Ціна": "5000"
    },
    2: {
        "Марка": "VW",
        "Модель": "Golf 5",
        "Рік": "2012",
        "Ціна": "7000"
    },
    3: {
        "Марка": "Audi",
        "Модель": "A4",
        "Рік": "2012",
        "Ціна": "12000"
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

    try:
        min_price = int(min_price)
        max_price = int(max_price)
    except ValueError:
        return HttpResponse("Некоректні параметри ціни")

    filtered_cars = []

    for car_id, car in cars.items():
        try:
            price = int(car["Ціна($)"].replace("$", ""))
            if min_price <= price <= max_price:
                filtered_cars.append(car)
        except ValueError:
            continue

    result = "<h2>Знайдені авто:</h2>"
    if filtered_cars:
        result += "<ul>"
        for car in filtered_cars:
            result += f"<li>Марка: {car['Марка']}, Модель: {car['Модель']}, Рік: {car['Рік']}, Ціна: ${car['Ціна($)']}</li>"
        result += "</ul>"
    else:
        result += "<p>Авто не знайдено за заданими критеріями.</p>"

    return HttpResponse(result)


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
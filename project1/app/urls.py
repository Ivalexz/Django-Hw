from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
path('', views.hello_world, name='hello_world'),#http://127.0.0.1:8000
    path('info/', views.show_info, name='show_info'),#http://127.0.0.1:8000/info
    path('hello/<str:name>/', views.say_hello, name='say_hello'),#http://127.0.0.1:8000/hello/Ігор
    path('car/<int:car_id>/', views.show_car_by_id, name='show_car_by_id'),#http://127.0.0.1:8000/car/1
    path('car/search/', views.search_cars, name='search_cars'),#http://127.0.0.1:8000/car/search?min_price=6900
    path('greet/', views.greeting, name='greeting'),
]

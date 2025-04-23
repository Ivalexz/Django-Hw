import random

from django.http import HttpResponse
from django.template.defaultfilters import lower

books={
        1: {
            "name": "Вбивство на полі для гольфу",
            "author": "Агата Крісті",
            "genre": "детектив",
            "year": 1923,
            "price": 300
        },
        2:
            {
        "name": "Маленький принц",
        "author": "Антуан де Сент-Екзюпері",
        "genre": "філософська казка",
        "year": 1943,
        "price": 180
            },
    3:{
        "name": "Гордість і упередження",
        "author": "Джейн Остін",
        "genre": "роман",
        "year": 1813,
        "price": 250
    },
    4:{
        "name": "Портрет Доріана Грея",
        "author": "Оскар Вайльд",
        "genre": "готичний роман",
        "year": 1890,
        "price": 190
    },
        5:{
        "name": "451° за Фаренгейтом",
        "author": "Рей Бредбері",
        "genre": "антиутопія",
        "year": 1953,
        "price": 215
        }
    }

def show_main(request):
    return HttpResponse("<h1>Каталог книг</h1>")

def show_list_of_books(request):
    result = ""
    for book in books.values():
        result += f"""
            <h3>{book["name"]}</h3>
            <p>Автор: {book["author"]}</p>
            <p>Жанр: {book["genre"]}</p>
            <p>Рік: {book["year"]}</p>
            <p>Ціна: {book["price"]}</p>
            """
    return HttpResponse(f"<h2>Усі доступні книги:</h2>{result}")


def show_news(request):
    random_popular_books=[]
    count=0
    while count!=3:
        rand_id = random.choice(list(books.keys()))
        if books[rand_id] not in random_popular_books:
            random_popular_books.append(books[rand_id])
            count+=1
    result = ""
    for book in random_popular_books:
        result += f"""
                <h3>{book["name"]}</h3>
                <p>Автор: {book["author"]}</p>
                <p>Жанр: {book["genre"]}</p>
                <p>Рік: {book["year"]}</p>
                <p>Ціна: {book["price"]}</p>
                """
    return HttpResponse(f"<h2>Найпопулярніші новинки місяця: {result}</h2>")

def search_books_by_genre(request, genre):
    genre=lower(genre)
    searched = []
    for book in books.values():
        if genre in lower(book["genre"]):
            searched.append(book)

    result = ""
    for book in searched:
        result += f"""
                    <h3>{book["name"]}</h3>
                    <p>Автор: {book["author"]}</p>
                    <p>Жанр: {book["genre"]}</p>
                    <p>Рік: {book["year"]}</p>
                    <p>Ціна: {book["price"]}</p>
                    """
    return HttpResponse(f"<h2>Результати пошуку '{genre}': {result}</h2>")

def show_book_by_id(request, book_id):
    result=""
    format = request.GET.get('format', '')
    if book_id in books:
        result += f"""
                            <h3>{books[book_id]["name"]}</h3>
                            <p>Автор: {books[book_id]["author"]}</p>
                            <p>Жанр: {books[book_id]["genre"]}</p>
                            <p>Рік: {books[book_id]["year"]}</p>
                            <p>Ціна: {books[book_id]["price"]}</p>
                            """
        return HttpResponse(f"<h2>Результати пошуку за ID {book_id}: {result}</h2>")
    else:
        return HttpResponse(f"<h2>Книгу з ID {book_id} не знайдено</h2>")

def search_books_by_piece_of_name(request, piece_of_name):
    name=lower(piece_of_name)
    searched=[]
    for book in books.values():
        if name in lower(book["name"]):
                searched.append(book)

    result = ""
    for book in searched:
        result += f"""
                    <h3>{book["name"]}</h3>
                    <p>Автор: {book["author"]}</p>
                    <p>Жанр: {book["genre"]}</p>
                    <p>Рік: {book["year"]}</p>
                    <p>Ціна: {book["price"]}</p>
                    """
    return HttpResponse(f"<h2>Результати пошуку за частиною назви'{name}': {result}</h2>")

def filter_by_price(request):
    min_price = int(request.GET.get("min_price"))
    max_price = int(request.GET.get("max_price"))

    filtered = list(filter(lambda book: min_price <= int(book["price"]) <= max_price, books.values()))

    if filtered:
        result = ""
        for book in filtered:
            result += f"""
                <h3>{book["name"]}</h3>
                <p>Автор: {book["author"]}</p>
                <p>Жанр: {book["genre"]}</p>
                <p>Ціна: {book["price"]} грн</p>
            """
        return HttpResponse(f"<h2>Книги з ціною від {min_price} до {max_price}</h2>{result}")
    else:
        return HttpResponse("<p>Введіть діапазон цін для пошуку!</p>")

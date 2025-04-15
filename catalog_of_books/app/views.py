import random

from django.http import HttpResponse
from django.template.defaultfilters import lower

books=[
    {
        "name": "Вбивство на полі для гольфу",
        "author": "Агата Крісті",
        "genre": "детектив",
        "year": 1923
    },
    {
        "name": "Маленький принц",
        "author": "Антуан де Сент-Екзюпері",
        "genre": "філософська казка",
        "year": 1943
    },
{
        "name": "Гордість і упередження",
        "author": "Джейн Остін",
        "genre": "роман",
        "year": 1813
    },
{
        "name": "Портрет Доріана Грея",
        "author": "Оскар Вайльд",
        "genre": "готичний роман",
        "year": 1890
    },
    {
        "name": "451° за Фаренгейтом",
        "author": "Рей Бредбері",
        "genre": "антиутопія",
        "year": 1953
    },
]
def show_main(request):
    return HttpResponse("<h1>Каталог книг</h1>")

def show_list_of_books(request):
    result = ""
    for book in books:
        result += f"""
            <h3>{book["name"]}</h3>
            <p>Автор: {book["author"]}</p>
            <p>Жанр: {book["genre"]}</p>
            <p>Рік: {book["year"]}</p>
            """
    return HttpResponse(f"<h2>Усі доступні книги:</h2>{result}")


def show_news(request):
    random_popular_books=[]
    count=0
    while count!=3:
        random_index=random.randint(0, len(books)-1)
        if books[random_index] not in random_popular_books:
            random_popular_books.append(books[random_index])
            count+=1
    result = ""
    for book in random_popular_books:
        result += f"""
                <h3>{book["name"]}</h3>
                <p>Автор: {book["author"]}</p>
                <p>Жанр: {book["genre"]}</p>
                <p>Рік: {book["year"]}</p>
                """
    return HttpResponse(f"<h2>Найпопулярніші новинки місяця: {result}</h2>")

def search_books(request, genre):
    genre=lower(genre)
    searched=[]
    for book in books:
        if genre in lower(book["genre"]):
            searched.append(book)

    result = ""
    for book in searched:
        result += f"""
                    <h3>{book["name"]}</h3>
                    <p>Автор: {book["author"]}</p>
                    <p>Жанр: {book["genre"]}</p>
                    <p>Рік: {book["year"]}</p>
                    """
    return HttpResponse(f"<h2>Результати пошуку '{genre}': {result}</h2>")

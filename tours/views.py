import random
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from tours.data import tours, departures, title, subtitle, description


def main_view(request):
    random_indexes = random.sample(list(tours), 6)
    random_tours = [tours[i] for i in random_indexes]
    return render(request, "tours/index.html",
                  context={"tours": random_tours, "title": title, "subtitle": subtitle, "description": description})


def departure_view(request, departure):
    filtered_tours = [tour for tour in tours.values() if tour["departure"] == departure]
    min_price = min([tour["price"] for tour in filtered_tours])
    max_price = max([tour["price"] for tour in filtered_tours])
    min_nights = min([tour["nights"] for tour in filtered_tours])
    max_nights = max([tour["nights"] for tour in filtered_tours])
    title = departures[departure]
    return render(request, "tours/departure.html",
                  context={"tours": filtered_tours, "len": len(filtered_tours), "min_price": min_price,
                           "max_price": max_price, "min_nights": min_nights, "max_nights": max_nights, "title": title})


def tour_view(request, id):
    tour = tours[id]
    stars = range(int(tour["stars"]))
    return render(request, "tours/tour.html",
                  context={"tour": tour, "departure": departures[tour["departure"]], "range": stars})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

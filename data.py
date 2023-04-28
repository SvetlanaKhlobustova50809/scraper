import json
import parse

# def some_logic(lst):
#     res1 = sort_films_by_year(lst, True)
#     res2 = sort_films_by_year(lst, False)
#     res3 = count_films_by_year(lst, 2021)
#     return res3

#сортировка фильмов по году, flag = True по возрастанию, flag = False по убыванию
def sort_films_by_year(list_of_films_info, flag):
    list_of_films_and_year = {}
    for film in list_of_films_info:
        key = film['Film name']
        value = film['Year of the film']
        list_of_films_and_year[key]=value
    if flag:
        sorted_films = dict(sorted(list_of_films_and_year.items(),key=lambda x:x[1]))
    else:
        sorted_films = dict(reversed(sorted(list_of_films_and_year.items(),key=lambda x:x[1])))
    return sorted_films


#вывод инормации о том, сколько фильмов было снято в каждый год
def count_for_each_year(list_of_films):
    film_and_year = sort_films_by_year(list_of_films, True)
    res = {}
    for film_name in film_and_year:
        film_year = film_and_year[film_name]
        counter = 0
        for a in film_and_year:
            if film_and_year[a] == film_year:
                counter += 1
        if(film_and_year.get(film_year,0) == 0):
            res[film_year] = counter
    return res


#вывод количества фильмов за конкретный год
def count_films_by_year(list_of_films, year):
    result = 0
    for film in list_of_films:
        if film["Year of the film"] == year:
            result += 1
    return "{}: {}".format(year,result)


#вывод списка фильмов с оценкой выше установленной
def find_by_rate(list_of_films, rate):
    result = dict()
    for film in list_of_films:
        if (film["Rating"] >= rate):
            result[film["Film name"]] = film["Rating"]
    return result


#вывод списка фильмов в алфавитном порядке
def sort_in_alphabetical_order(list_of_films):
    result = {}
    for film in list_of_films:
        result[film["Film name"]] = film["Rating"]
    result = sorted(result)
    return result

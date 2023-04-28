from download import Downloader
from parse import Parser
import json

from data import sort_in_alphabetical_order
from data import sort_films_by_year
from data import count_for_each_year
from data import count_films_by_year
from data import find_by_rate



def open_file(file):
    f = open(file,'r')
    temp = f.read()
    list_of_films = json.loads(temp)
    return list_of_films

def process(url, web_page_path="html_file", data_path="json_file"):
    downloader = Downloader(url)
    downloader.save(web_page_path)

    parser = Parser(web_page_path)
    parser.parse()
    parser.save(data_path)

    data = open_file(data_path)
    return find_by_rate(data, 8.5)

print(process('https://m.imdb.com/chart/top/'))

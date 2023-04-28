from bs4 import BeautifulSoup
import json

class Parser:
    json_string = ""
    def __init__(self, file_path):
        self.file_path = file_path
    def open_file(self):
        f = open(self.file_path)
        result = f.read()
        return result
    def parse(self):
        result = self.open_file()
        soup = BeautifulSoup(result, "html.parser")

        list_of_h4 = soup.find_all("h4")
        list_of_h4_unhold = soup.find_all("span", class_ = "imdb-rating")
        
        list_of_films = []

        for j in range(len(list_of_h4)):
            block = list_of_h4[j]
            rating = float(list_of_h4_unhold[j].text.split()[0])
            film_info = block.text.split()
            film_number_in_top = int(film_info[0][:-1])
            film_year = int(film_info[-1][1:-1:])
            name = ""
            for i in range(1, len(film_info) - 2):
                word = film_info[i]
                name += word + ' '
            name += film_info[len(film_info) - 2]
            d = {"Film name" : name, "Film position in top list" : film_number_in_top, "Rating" : rating, "Year of the film": film_year}
            list_of_films.append(d)
        jsn = json.dumps(list_of_films, ensure_ascii=False, indent=4)
        self.json_string = jsn

    def save(self, parsed_file_path):
        f = open(parsed_file_path, "w")
        f.write(self.json_string)


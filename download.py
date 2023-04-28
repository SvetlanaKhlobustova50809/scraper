import requests


class Downloader:
    def __init__(self, url, params=None, method="GET"):
        self.url = url
        self.params = params
        self.method = method

    def get_html(self):
        response = requests.request(method=self.method, url=self.url, params=self.params)
        return response.text

    def save(self, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.get_html())

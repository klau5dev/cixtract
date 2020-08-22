import requests

class Cixtract():
    def crawl(self, url: str):
        res = requests.get(url)
        return res

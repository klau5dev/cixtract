import requests

class Cixtract():
    def crawl(self, url: str) -> requests.Response:
        res = requests.get(url)
        return res

    def get_readme(self, repo: str) -> str:
        url = "https://raw.githubusercontent.com/{}/master/README.md"

        path = repo.replace("https://github.com/", "")
        url = url.format(path)

        try:
            res = self.crawl(url)
            if res.status_code >= 400:
                result = ""
            else:
                result = res.text
        except:
            result = ""

        return result

import requests

class CixtractError(Exception):
    pass
class DoesNotExist(CixtractError):
    pass

class Cixtract():
    def crawl(self, url: str) -> str:
        try:
            res = requests.get(url)
        except:
            raise DoesNotExist

        if res.status_code >= 400:
            raise DoesNotExist

        return res.text
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

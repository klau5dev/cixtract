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

    def extract_path(self, repo: str) -> str:
        return repo.replace("https://github.com/", "")

    def get_readme(self, repo: str) -> str:
        url = "https://raw.githubusercontent.com/{}/master/README.md"
        path = self.extract_path(repo)
        url = url.format(path)

        return self.crawl(url)

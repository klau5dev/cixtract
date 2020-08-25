import requests
from typing import Dict

class CixtractError(Exception):
    pass
class DoesNotExist(CixtractError):
    pass

class Cixtract():
    def crawl(self, url: str, headers: Dict = None) -> str:
        if headers is None:
            headers = {}
        if headers.get("User-Agent", None) is None:
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36"

        try:
            res = requests.get(url, headers=headers)
        except:
            raise DoesNotExist

        if res.status_code >= 400:
            raise DoesNotExist

        return res.text

    def extract_repo_path(self, repo: str) -> str:
        return repo.replace("https://github.com/", "")

    def get_readme(self, repo: str) -> str:
        url = "https://raw.githubusercontent.com/{}/master/README.md"
        path = self.extract_repo_path(repo)
        url = url.format(path)

        return self.crawl(url)

    def guess_travis(self, repo: str) -> str:
        url = "https://api.travis-ci.org/repo/{}"
        path = self.extract_repo_path(repo)
        url = url.format(path.replace("/", "%2F"))

        headers = {"Travis-API-Version": "3"}

        try:
            _ = self.crawl(url, headers)
        except DoesNotExist as exception:
            raise exception

        return "https://travis-ci.org/{}".format(path)

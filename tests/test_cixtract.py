from unittest import TestCase

from cixtract import Cixtract

class CixtractTest(TestCase):
    def test_crawl(self):
        cixtract = Cixtract()

        url = "https://raw.githubusercontent.com/klau5dev/cixtract/master/README.md"
        with open("README.md") as f:
            result = f.read()

        res = cixtract.crawl(url)
        self.assertEqual(res.text, result)

    def test_get_readme(self):
        cixtract = Cixtract()

        repo = "https://github.com/klau5dev/cixtract"
        with open("README.md") as f:
            result = f.read()

        res = cixtract.get_readme(repo)
        self.assertEqual(res, result)

        repo = "https://github.com/klau5dev/not_exist"
        res = cixtract.get_readme(repo)
        self.assertEqual(res, "")


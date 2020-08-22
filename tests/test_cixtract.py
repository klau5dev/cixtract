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

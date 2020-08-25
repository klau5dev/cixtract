from unittest import TestCase

from cixtract import Cixtract, DoesNotExist

class CixtractTest(TestCase):
    def test_crawl(self):
        cixtract = Cixtract()

        url = "https://raw.githubusercontent.com/klau5dev/cixtract/master/README.md"
        with open("README.md") as f:
            result = f.read()

        res = cixtract.crawl(url)
        self.assertEqual(res, result)

        url = "https://raw.githubusercontent.com/klau5dev/not_exist/master/README.md"
        self.assertRaises(DoesNotExist, cixtract.crawl, url)


        for test in testcase:
            res = cixtract.get_readme(test[0])
            self.assertEqual(res, test[1])


        res = cixtract.get_readme(repo)
        self.assertEqual(res, result)

        repo = "https://github.com/klau5dev/not_exist"
        res = cixtract.get_readme(repo)
        self.assertEqual(res, "")


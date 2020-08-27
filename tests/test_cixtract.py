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

    def test_extract_repo_path(self):
        cixtract = Cixtract()
        url = "https://github.com/klau5dev/cixtract"

        result = cixtract.extract_repo_path(url)
        self.assertEqual(result, "klau5dev/cixtract")

    def test_get_readme(self):
        cixtract = Cixtract()

        url = "https://github.com/klau5dev/cixtract"

        with open("README.md") as f:
            result = f.read()

        res = cixtract.get_readme(url)
        self.assertEqual(res, result)

        url = "https://github.com/klau5dev/not_exist"
        self.assertRaises(DoesNotExist, cixtract.get_readme, url)

    def test_guess_travis(self):
        cixtract = Cixtract()

        url = "https://github.com/klau5dev/cixtract"
        res = cixtract.guess_travis(url)
        self.assertEqual(res, "https://travis-ci.org/klau5dev/cixtract")

        url = "https://github.com/klau5dev/not_exist"
        self.assertRaises(DoesNotExist, cixtract.guess_travis, url)

    def test_parse_readme(self):
        cixtract = Cixtract()

        with open("README.md") as f:
            content = f.read()

        res = cixtract.parse_readme(content)

        self.assertEqual(res, {"Travis-ci":["https://travis-ci.org/klau5dev/cixtract"]})

    def test_get_ci(self):
        cixtract = Cixtract()

        url = "https://github.com/klau5dev/cixtract"
        res = cixtract.get_ci(url)
        self.assertEqual(res, {"Travis-ci":["https://travis-ci.org/klau5dev/cixtract"]})

        url = "https://github.com/klau5dev/not_exist"
        res = cixtract.get_ci(url)
        self.assertEqual(res, {})

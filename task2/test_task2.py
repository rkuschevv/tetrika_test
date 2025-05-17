import csv
import os
import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from .solution import WikiAnimalScraper


class TestWikiAnimalScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WikiAnimalScraper()

    def test_initialization(self):
        self.assertEqual(self.scraper.BASE_URL, "https://ru.wikipedia.org")
        self.assertEqual(
            self.scraper.CATEGORY_URL,
            "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
        )
        self.assertEqual(len(self.scraper.animals_by_letter), 0)
        self.assertIsNotNone(self.scraper.session)

    def test_get_page_content(self):
        with patch.object(self.scraper, "session") as mock_session:
            mock_response = MagicMock()
            mock_response.text = "Test content"
            mock_session.get.return_value = mock_response

            soup = self.scraper.get_page_content("https://test.url")
            self.assertEqual(soup.text, "Test content")

    def test_process_page(self):
        with patch.object(self.scraper, "get_page_content") as mock_get_content:
            mock_soup = BeautifulSoup("""
            <html>
                <div id="mw-pages">
                    <div class="mw-category">
                        <div class="mw-category-group">
                            <a href="/wiki/Аист">Аист</a>
                            <a href="/wiki/Барс">Барс</a>
                            <a href="/wiki/Волк">Волк</a>
                        </div>
                    </div>
                    <a href="/wiki/Next">Следующая страница</a>
                </div>
            </html>
            """, "html.parser")
            mock_get_content.return_value = mock_soup

            next_url = self.scraper.process_page(self.scraper.CATEGORY_URL)

            self.assertEqual(len(self.scraper.animals_by_letter["А"]), 1)
            self.assertEqual(len(self.scraper.animals_by_letter["Б"]), 1)
            self.assertEqual(len(self.scraper.animals_by_letter["В"]), 1)
            self.assertEqual(next_url, self.scraper.BASE_URL + "/wiki/Next")

    def test_save_to_csv(self):
        self.scraper.animals_by_letter["А"].add("Аист")
        self.scraper.animals_by_letter["Б"].add("Барс")
        self.scraper.animals_by_letter["В"].add("Волк")

        test_file = "test_beasts.csv"
        self.scraper.save_to_csv(test_file)

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            data = list(reader)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[0], ["А", "1"])
            self.assertEqual(data[1], ["Б", "1"])
            self.assertEqual(data[2], ["В", "1"])

        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()

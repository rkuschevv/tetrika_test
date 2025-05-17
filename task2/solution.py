import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import csv
import re
from typing import Dict, Set


class WikiAnimalScraper:
    BASE_URL = "https://ru.wikipedia.org"
    CATEGORY_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"

    def __init__(self):
        self.animals_by_letter: Dict[str, Set[str]] = defaultdict(set)
        self.session = requests.Session()

    def get_page_content(self, url: str) -> BeautifulSoup:
        response = self.session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def process_page(self, url: str) -> str | None:
        soup = self.get_page_content(url)
        content_div = soup.find('div', id='mw-pages')
        if not content_div:
            return None

        for link in content_div.find_all('a'):
            animal_name = link.text.strip()
            if animal_name and len(animal_name) > 0:
                first_letter = animal_name[0].upper()
                if re.match(r'[А-Я]', first_letter):
                    self.animals_by_letter[first_letter].add(animal_name)

        next_link = soup.find('a', string='Следующая страница')
        if next_link:
            return self.BASE_URL + next_link['href']
        return None

    def scrape_animals(self):
        current_url = self.CATEGORY_URL
        while current_url:
            current_url = self.process_page(current_url)

    def save_to_csv(self, filename: str = 'beasts.csv'):
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            for letter in sorted(self.animals_by_letter.keys()):
                writer.writerow([letter, len(self.animals_by_letter[letter])]) 
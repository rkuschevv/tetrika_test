from solution import WikiAnimalScraper


def main():
    print("Начат парсинг")
    scraper = WikiAnimalScraper()
    scraper.scrape_animals()
    scraper.save_to_csv()
    print("Парсинг завершен. Результаты сохранены в файл beasts.csv")


if __name__ == '__main__':
    main()

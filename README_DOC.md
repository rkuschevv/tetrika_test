# Документация по запуску решений

## Установка и запуск

Проект можно запустить двумя способами: через Poetry или через Docker.

### Способ 1: Использование Poetry

1. Установите Poetry, если он еще не установлен:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Установите зависимости:
```bash
poetry install
```

3. Запуск тестов для всех задач:
```bash
poetry run pytest -v
```

### Способ 2: Использование Docker

1. Убедитесь, что у вас установлены Docker и Docker Compose

2. Запуск всех тестов:
```bash
docker-compose up tests
```

3. Запуск конкретной задачи:
```bash
docker-compose up task1  # Для первой задачи
docker-compose up task2  # Для второй задачи
docker-compose up task3  # Для третьей задачи
```

## Задача 1: Декоратор @strict

Декоратор для проверки типов аргументов и возвращаемого значения функции.

### Запуск тестов
```bash
# Через Poetry:
poetry run pytest task1/test_solution.py -v

# Через Docker:
docker-compose up task1
```

### Пример использования
```python
from task1.solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# Корректный вызов
result = sum_two(1, 2)  # Вернет 3

# Некорректный вызов вызовет TypeError
sum_two(1, 2.4)  # Вызовет TypeError
```

## Задача 2: Парсер животных с Википедии

Скрипт для сбора статистики о количестве животных на каждую букву алфавита с русскоязычной Википедии.

### Запуск парсера и тестов
```bash
# Через Poetry:
poetry run python task2/run_scraper.py
poetry run pytest task2/test_solution.py -v

# Через Docker:
docker-compose up task2
```

После выполнения скрипта будет создан файл `beasts.csv` со статистикой в формате:
```
А,1299
Б,1780
...
```

## Задача 3: Подсчет времени присутствия

Функция для расчета общего времени присутствия ученика и преподавателя на уроке.

### Запуск тестов
```bash
# Через Poetry:
poetry run pytest task3/test_solution.py -v

# Через Docker:
docker-compose up task3
```

### Пример использования
```python
from task3.solution import appearance

test_data = {
    'intervals': {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    }
}

result = appearance(test_data)  # Вернет 3117
```

## Структура проекта

```
├── pyproject.toml         # Конфигурация Poetry и зависимости
├── docker-compose.yml     # Конфигурация Docker Compose
├── Dockerfile            # Конфигурация Docker образа
├── task1/
│   ├── solution.py        # Реализация декоратора @strict
│   └── test_solution.py   # Тесты для декоратора
├── task2/
│   ├── solution.py        # Реализация парсера Wikipedia
│   ├── run_scraper.py     # Скрипт для запуска парсера
│   └── test_solution.py   # Тесты для парсера
└── task3/
    ├── solution.py        # Реализация расчета времени
    └── test_solution.py   # Тесты для расчета времени
```

## Требования

- Python 3.12 или выше
- Poetry или Docker
- Зависимости (устанавливаются автоматически через Poetry или Docker):
  - beautifulsoup4 4.12.3 (для парсинга HTML)
  - requests 2.31.0 (для HTTP-запросов)
  - pytest 8.0.2 (для тестирования)

## Примечания

1. Все решения содержат подробные тесты, которые также служат примерами использования.
2. Файл `beasts.csv` создается заново при каждом запуске парсера.
3. Количество животных в результатах может меняться, так как данные берутся с живого сайта Википедии.
4. При использовании Poetry убедитесь, что вы находитесь в корневой директории проекта.
5. При использовании Docker все команды нужно выполнять из директории с файлом docker-compose.yml. 
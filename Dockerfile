FROM python:3.12-slim

# Установка Poetry
RUN pip install poetry

# Установка рабочей директории
WORKDIR /app

# Копирование файлов конфигурации
COPY pyproject.toml poetry.lock* ./

# Установка зависимостей
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копирование исходного кода
COPY . .

# Команда по умолчанию - запуск тестов
CMD ["poetry", "run", "pytest", "-v"] 
from tests.conftest import category_fruits

# Online_store_project
## Описание:
Online_store_project — это ядро каталога товаров для интернет-магазина.


## Установка
#### Клонируйте репозиторий:
```bash
git clone https://github.com/anton-pugachev-sigma/Online_store_project
```

#### Установите poetry:
```bash
pip install poetry
```

#### Установите все зависимости:
```bash
poetry install
```

## Тестирование
#### Запуск всех тестов
```bash
poetry run pytest
```

#### Запуск тестов с отчетом о покрытии кода
```bash
poetry run pytest --cov=src --cov-report=html
```

#### Запуск форматеров
```bash
poetry run black .
poetry run isort .
```

#### Запуск линтеров
```bash
poetry run flake8 .
poetry run mypy .
```


## Документация
#### В пакете src содержатся модули:
```category.py``` - содержит класс для категорий магазина

```product.py``` - содержит класс для представления продуктов магазина

```grass.py``` - содержит дочерний класс Product для представления товаров газона

```smartphone.py``` - содержит дочерний класс Product для представления телефонов

```read_data.py``` - содержит функцию, считывающую данные о категории из json file и создающая класс Category

```mixin_log.py``` - содержит класс, который выводит объект класса с его параметрами при создании

```base_product.py``` - содержит абстрактный класс для представления всех продуктов



#### Примеры использования category.py and product.py (каталога магазина)
```python
from src.product import Product
from src.category import Category

# 1. Инициализация товаров и категории
apple = Product("apple", "red fruit", 100, 100) # создаем объект класса Product
banana = Product("banana", "sweet yellow fruit", 30, 50)
cherry = Product("cherry", "purple berry", 100, 250)
category_fruits = Category("fruits", "fresh fruits", [apple, banana, cherry]) # создаем объект класса Category
# При объявлении продукта с нулевым кол-вом
# программа упадёт с ошибкой ValueError("Товар с нулевым количеством не может быть добавлен")
bad_product = Product("apple", "red fruit", 100, 0)

# 2. Работа со свойствами и методами
#Получение данных класса
apple.price = 20 # устанавливаем новую цену для продукта
products = category_fruits.products #получаем список товаров в виде единой строки

total_amount = apple.total_amount + banana.total_amount # вычисляем общую сумму произведений цены на количество у двух объектов.

#Высчитывание среднего ценника продуктов категории
average_price_fruits = category_fruits.count_average_price() # в нашём случае получим ответ 50.0

#Если в категории нет товаров, то мы получим ответ 0
snacks = Category("snacks", "harmful food", [])
average_price_snacks = snacks.count_average_price() # 0

#3. Отладка
print(repr(apple)) # получаем отладочный вывод для инициализации объекта класса Product





```


#### Примеры использования grass.py and smartphone.py:
```python
from src.grass import Grass
from src.smartphone import Smartphone

#Инициализация экземпляров классов
iphone = Smartphone(
    "Blue iphone",
    "Powerful phone",
    100_000,
    250,
    150,
    "Iphone 18",
    "32 Гб",
    "Blue")
poco = Smartphone(
        "Poco X6 black",
        "Big smartphone",
        60_000,
        1000,
        100,
        "Poco X6",
        "16 Гб",
        "Black",
    )

shadow_grass = Grass(
        "Луговой бархат",
        "Травосмесь для затененных участков и парковых зон",
        1800,
        30,
        "Russia",
        21,
        "Light green",
    )

emerald_grass = Grass(
        "emerald_grass", "green grass", 1500, 150, "Germany", 14, "Dark green"
    )

#Вычисляем сумму товаров одной категории (Можем складывать только те товары, которые относят к 1 категории)
total_grasses = emerald_grass + shadow_grass
total_smartphones = iphone + poco
```

#### Пример использования read_data.py
```python
from src.read_data import read_data_file

#Считываем данные и создаём список категорий на их основе
categories = read_data_file()
```


#### Пример использования base_product.py
```python
from src.base_product import BaseProduct

# Создаём класс на основе BaseProduct

class Car(BaseProduct):
    brand: str
    year: int

   #Если мы не укажем dunder метод __init__ программа упадёт с ошибкой
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

```


#### Пример использования mixin_log.py 
```python
from src.smartphone import Smartphone
from src.product import Product

# Создаём объекта класс Product и получаем дебажный вывод
car = Product('Kia', 'Red car', 1000000, 200)

# Вывод: Product('Kia', 'Red car', 1000000, 200)

# Миксин автоматически работает и для всех классов-наследников
phone = Smartphone('Poco X6', 'Big smartphone', 60000, 1000, 100, 'X6', '16 Гб', 'Black')
# Вывод: Smartphone('Poco X6', 'Big smartphone', 60000, 1000)
```
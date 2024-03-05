class Flower:
    def __init__(self, name, color, stem_length, freshness, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price

    def __repr__(self):
        return f"{self.name}"


class Rose(Flower):
    def __init__(self, name, color, stem_length, freshness, price):
        super().__init__(name, color, stem_length, freshness, price)

    is_thorny = True


class Tulip(Flower):
    def __init__(self, name, color, stem_length, freshness, price):
        super().__init__(name, color, stem_length, freshness, price)


class Peon(Flower):
    def __init__(self, name, color, stem_length, freshness, price):
        super().__init__(name, color, stem_length, freshness, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def bouquet_cost(self):
        total = 0
        for flower in self.flowers:
            total += flower.price
        return total

    def average_longevity(self):
        longevity = 0
        for flower in self.flowers:
            longevity += flower.freshness
        return longevity / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))
        return self.flowers

    def search_flowers(self, key, value):
        result = []
        for flower in self.flowers:
            if str(value).lower() in str(getattr(flower, key)).lower():
                result.append(flower)
        return result


rose = Rose('Роза индийская', 'красный', 45, 8, 10)
tulip = Tulip('Тюльпан испанский', 'желтый', 30, 7, 7)
peon = Peon('Пион кустарный', 'розовый', 40, 10, 5)

bouquet = Bouquet()
bouquet.add_flowers(rose)
bouquet.add_flowers(tulip)
bouquet.add_flowers(peon)
print(f'Цена: {bouquet.bouquet_cost()}')
sort_type = input('Введите вариант сортировки: name / price / stem_length / freshness ')
print(f'Сортируем по свежести: {bouquet.sort_flowers(key=sort_type)}')
print(f'Среднее время жизни букета: {round(bouquet.average_longevity())}')
search_type, search_value = input('Введите параметр: name / price / stem_length / freshness и значение ').split()
print(f'Ищем по {search_type}: {bouquet.search_flowers(search_type, search_value)}')

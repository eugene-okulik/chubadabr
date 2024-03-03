class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, name, author, page_count, ISBN, is_reserved):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.ISBN = ISBN
        self.is_reserved = is_reserved


class SchoolBook(Book):
    def __init__(self, name, author, page_count, ISBN, is_reserved, subject, group, is_with_tasks):
        super().__init__(name, author, page_count, ISBN, is_reserved)
        self.subject = subject
        self.group = group
        self.is_with_tasks = is_with_tasks


posoh_i_shlapa = Book('Посох и шляпа', 'Терри Пратчетт', 384, '978-5-699-16610-7', False)
vladichica_ozera = Book('Владычица Озера', 'Анджей Сапковский', 544, '978-5-17-121727-3', False)
picnic_na_obochine = Book('Пикник на обочине', 'Аркадий Стругацкий, Борис Стругацкий', 256, '978-5-17-114346-6', False)
dnd_players_book_5e = Book('Dungeons & Dragons. Книга игрока', 'WoTC', 320, '978-5-6041656-8-3', False)
book_1984 = Book('1984', 'Джордж Оруэлл', 320, '978-5-17-150043-6', False)
books = (posoh_i_shlapa, vladichica_ozera, picnic_na_obochine, dnd_players_book_5e, book_1984)
vladichica_ozera.is_reserved = True

geography_7 = SchoolBook('География. Материки и океаны', 'Елена Кольмакова', 239, '978-985-599-715-4',
                         False, 'География', 7, True)
algebra_10 = SchoolBook('Алгебра и начала анализа', 'Иванова А.И.', 315, '978-1-234567-89-0', False,
                        'Алгебра', 10, True)
russian_lang_11 = SchoolBook('Русский язык', 'Петров П.П.', 422, '978-2-345678-90-1', False, 'Русский язык', 11, True)
history_12 = SchoolBook('Мировая история', 'Сидоров С.С.', 218, '978-3-456789-01-2', False, 'История', 12, True)
SchoolBooks = (geography_7, algebra_10, russian_lang_11, history_12)
algebra_10.is_reserved = True


def printer(book):
    if hasattr(book, 'group'):
        if book.is_reserved:
            print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.page_count}, "
                  f"предмет: {book.subject}, класс: {book.group}, зарезервирована")
        else:
            print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.page_count}, "
                  f"предмет: {book.subject}, класс: {book.group}")
    else:
        if book.is_reserved:
            print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.page_count}, "
                  f"материал: {book.page_material}, зарезервирована")
        else:
            print(f"Название: {book.name}, "
                  f"Автор: {book.author}, страниц: {book.page_count}, материал: {book.page_material}")


for book in books:
    printer(book)
print()
for book in SchoolBooks:
    printer(book)

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Тест 1: Проверка добавления книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Тест 2: Нельзя добавить одну и ту же книгу дважды
    def test_add_new_book_add_the_same_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги и третью такую же, как вторая
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что третья книга не добавилась
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Тест 3: Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_book_not_exist(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить',5)

        # проверяем, что при назначении рейтинга несуществующей книге, не добавится новый элемент в коллекцию
        assert len(collector.get_books_rating()) == 1

    # Тест 4: Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_book_less_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        # проверяем, что при назначении рейтинга меньше 1, рейтинг не назначится книге
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Тест 5: Нельзя выставить рейтинг больше 10
    def test_set_book_rating_book_more_ten(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)

        # проверяем, что при назначении рейтинга больше 10, рейтинг не назначится книге
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Тест 6: У не добавленной книги нет рейтинга
    def test_get_book_rating_book_not_exist(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # проверяем, что не у не добавленной книги нет рейтинга
        assert not collector.get_book_rating('Кошкин дом')

    # Тест 7: Добавление книги в избранное
    def test_add_book_in_favorites_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем три книги и две из них в избранные
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кошкин дом')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # проверяем, что две книги добавлены в избранные
        assert len(collector.get_list_of_favorites_books()) == 2

    # Тест 8: Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_not_exist_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в избранные, если её нет в словаре books_rating
        collector.add_book_in_favorites('Кошкин дом')

        # проверяем, что книга не добавлена в избранные
        assert len(collector.get_list_of_favorites_books()) == 0

    # Тест 9: Проверка удаления книги из избранного
    def test_delete_book_from_favorites_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги, добавляем их в избранные и удалем одну книгу из избранных
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга удалена из избранных
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тест 10: Выводим список книг с определенным рейтингом
    def test_get_books_with_specific_rating_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем три книги, одной из них меняем рейтинг
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кошкин дом')
        collector.set_book_rating('Кошкин дом', 10)

        # проверяем, что найдется две книги с рейтингом 1
        assert len(collector.get_books_with_specific_rating(1)) == 2

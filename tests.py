import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_the_same_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2, "О нет, книга добавилась дважды!"

    def test_set_book_rating_book_not_exist(self):
        collector = BooksCollector()

        collector.set_book_rating('Что делать, если ваш кот хочет вас убить',5)

        assert not collector.get_book_rating('Что делать, если ваш кот хочет вас убить')

    @pytest.mark.parametrize(
        "book_name,rating",
        [
            ['Гордость и предубеждение и зомби', 0],
            ['Что делать, если ваш кот хочет вас убить', 11]
        ]
    )
    def test_set_book_rating_not_in_range_0_10(self, book_name, rating):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        assert collector.get_book_rating(book_name) == 1

    def test_get_book_rating_book_not_exist(self):
        collector = BooksCollector()

        assert not collector.get_book_rating('Кошкин дом')

    def test_add_book_in_favorites_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кошкин дом')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_not_exist_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Кошкин дом')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_books_with_specific_rating_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кошкин дом')
        collector.set_book_rating('Кошкин дом', 10)

        assert len(collector.get_books_with_specific_rating(1)) == 2

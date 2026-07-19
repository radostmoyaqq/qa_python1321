import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Pride and Prejudice and Zombies')
        collector.add_new_book('How to Tell If Your Cat Is Plotting')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'a' * 41])
    def test_add_new_book_invalid_name_length_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_add_new_book_same_book_twice_added_once(self):
        collector = BooksCollector()

        collector.add_new_book('Dune')
        collector.add_new_book('Dune')

        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre_added_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Dune')

        assert collector.get_book_genre('Dune') == ''

    def test_set_book_genre_existing_book_valid_genre_sets_genre(self):
        collector = BooksCollector()
        genre = collector.genre[0]

        collector.add_new_book('Dune')
        collector.set_book_genre('Dune', genre)

        assert collector.get_book_genre('Dune') == genre

    def test_set_book_genre_for_unknown_book_returns_none(self):
        collector = BooksCollector()
        genre = collector.genre[0]

        # Пытаемся установить жанр книге, которой нет в коллекции
        collector.set_book_genre('Unknown book', genre)

        assert collector.get_book_genre('Unknown book') is None

    def test_set_book_genre_unknown_genre_does_not_set(self):
        collector = BooksCollector()

        collector.add_new_book('Dune')
        # Пытаемся установить несуществующий в списке допустимых жанр
        collector.set_book_genre('Dune', 'Unknown genre')

        # Жанр должен остаться пустым, как при создании книги
        assert collector.get_book_genre('Dune') == ''

    def test_get_books_with_specific_genre_returns_books_with_genre(self):
        collector = BooksCollector()
        target_genre = collector.genre[3]
        other_genre = collector.genre[4]

        collector.add_new_book('The Lion King')
        collector.add_new_book('Home Alone')
        collector.set_book_genre('The Lion King', target_genre)
        collector.set_book_genre('Home Alone', other_genre)

        assert collector.get_books_with_specific_genre(target_genre) == ['The Lion King']

    def test_get_books_for_children_excludes_books_with_age_rating(self):
        collector = BooksCollector()
        children_genre = collector.genre[3]
        age_rating_genre = collector.genre_age_rating[0]

        collector.add_new_book('The Lion King')
        collector.add_new_book('It')
        collector.set_book_genre('The Lion King', children_genre)
        collector.set_book_genre('It', age_rating_genre)

        assert collector.get_books_for_children() == ['The Lion King']

    def test_add_book_in_favorites_existing_book_adds_book_once(self):
        collector = BooksCollector()

        collector.add_new_book('Dune')
        collector.add_book_in_favorites('Dune')
        collector.add_book_in_favorites('Dune')

        assert collector.get_list_of_favorites_books() == ['Dune']

    def test_delete_book_from_favorites_existing_book_deletes_book(self):
        collector = BooksCollector()

        collector.add_new_book('Dune')
        collector.add_book_in_favorites('Dune')
        collector.delete_book_from_favorites('Dune')

        assert collector.get_list_of_favorites_books() == []
import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book_with_huge_name_len(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу длина названия которой больше 41 символов
        collector.add_new_book('«Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, '
                               'моряка из Йорка, прожившего двадцать восемь лет в полном одиночестве '
                               'на необитаемом острове у берегов Америки близ устьев реки Ориноко, куда '
                               'он был выброшен кораблекрушением, во время которого весь экипаж корабля, '
                               'кроме него, погиб, с изложением его неожиданного освобождения пиратами; '
                               'написанные им самим»')

        # проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_empty_name(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу без названия
        collector.add_new_book('')

        # проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Комедии'],
            ['Убийство в восточном экспрессе', 'Детективы'],
            ['Звездный путь', 'Фантастика']
        ])
    def test_set_book_genre_add_four_books_known_genre(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name, genre in collector.get_books_genre()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Человек-зверь', 'Триллер'],
            ['Щегол', 'Роман'],
            ['Ведьмак', 'Фэнтези'],
            ['Моя удивительная жизнь', 'Автобиография']
        ])
    def test_set_book_genre_add_four_books_unknown_genre(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name, genre not in collector.get_books_genre()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Комедии'],
            ['Убийство в восточном экспрессе', 'Детективы'],
            ['Звездный путь', 'Фантастика']
        ])
    def test_get_book_genre_four_books(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre().get(name) == genre

    def test_genre_list_is_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_is_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name, genre',
        [
            ['Валли', 'Мультфильмы'],
            ['Что делать, если ваш кот хочет вас убить', 'Комедии'],
            ['Убийство в восточном экспрессе', 'Детективы'],
            ['Звездный путь', 'Фантастика']
        ])
    def test_get_books_with_specific_genre_four_genres_check(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем книгу с жанром ужасы
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre)[0] == name

    def test_get_books_genre_add_three_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        books_names = ['Валли', 'Дюна', 'Оно']
        books_genres = ['Мультфильмы', 'Фантастика', 'Ужасы']
        books_with_genres = {'Валли': 'Мультфильмы', 'Дюна': 'Фантастика', 'Оно': 'Ужасы'}
        for i in range(3):
            name = books_names[i]
            genre = books_genres[i]
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == books_with_genres

    def test_get_books_for_children_three_books_from_four(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        books_names = ['Валли', 'Дюна', 'Оно', 'Трое из Простоквашино']
        books_genres = ['Мультфильмы', 'Фантастика', 'Ужасы', 'Мультфильмы']
        books_for_children = ['Валли', 'Дюна', 'Трое из Простоквашино']
        for i in range(4):
            name = books_names[i]
            genre = books_genres[i]
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == books_for_children

    def test_add_book_in_favorites_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Человек-зверь')
        collector.add_new_book('Сага о Форсайтах')

        # добавляем книги в избранное
        collector.add_book_in_favorites('Человек-зверь')
        collector.add_book_in_favorites('Сага о Форсайтах')
        # проверяем, что добавилось именно две
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_one_book_remain(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Щегол')
        collector.add_new_book('Ведьмак')

        # добавляем книги в избранное
        collector.add_book_in_favorites('Щегол')
        collector.add_book_in_favorites('Ведьмак')
        # удаляем вторую книгу
        collector.delete_book_from_favorites('Ведьмак')

        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        name_1 = 'Человек-зверь'
        name_2 = 'Сага о Форсайтах'

        # добавляем две книги
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)

        # добавляем книги в избранное
        collector.add_book_in_favorites(name_1)
        collector.add_book_in_favorites(name_2)

        assert collector.get_list_of_favorites_books() == [name_1, name_2]






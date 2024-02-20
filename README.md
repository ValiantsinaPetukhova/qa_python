# qa_python
test_genre_list_is_true - проверка списка genre 
test_genre_age_rating_is_true - проверка списка genre_age_rating
test_add_new_book_add_two_books - проверка добавления книг в словарь
test_add_new_book_add_book_with_huge_name_len - проверка, что книги с названием больше 40 символов не добавляются в словарь
test_add_new_book_add_empty_name - проверка, что книги с пустым названием не добавляются в словарь
test_set_book_genre_add_four_books_known_genre - добавление книг с жанрами из списка genres
test_set_book_genre_add_four_books_unknown_genre - проверка, что книги с жанрами, которых нет в списке genres, не добавляются в словарь
test_get_book_genre_four_books - проверка, что по названию книги метод выводит ее жанр 
test_get_books_with_specific_genre_four_genres_check - тест для проверки метода, который выводит список книг определенного жанра
test_get_books_genre_add_three_books - проверка вывода текущего словаря books_genre
test_get_books_for_children_three_books_from_four - проверка метода, который формирует список книг для детей
test_add_book_in_favorites_two_books - тест для проверки метода, который добавляет книги в список избранных
test_delete_book_from_favorites_one_book_remain - проверка метода по удалению книги из списка избранных
test_get_list_of_favorites_books_two_books - проверка метода, который возвращает список избранных книг.
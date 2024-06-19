from django.urls import path

from .views import (
    update_user_and_author,
    get_authors,
    author_detail,
    delete_author,
    create_book,
    update_book, 
    get_all_books,
    get_book,
    delete_book
)


urlpatterns = [
    path('authors/', get_authors, name="get-authors"),
    path('update-author/<int:pk>', update_user_and_author, name="update-author"),
    path('author-detail/<int:pk>', author_detail, name="author-detail"),
    path('delete-author/<int:pk>', delete_author, name="delete-author"),
    path('create-book', create_book, name="create-book"),
    path('update-book/<int:pk>', update_book, name="update-book"),
    path('all-books/', get_all_books, name="get-all-books"),
    path('get-book/<int:pk>', get_book, name="get-book"),
    path('delete-book/<int:pk>', delete_book, name="delete-book"),
]

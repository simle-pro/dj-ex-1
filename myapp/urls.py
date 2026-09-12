from django.urls import path
from .views import *

urlpatterns = [
    path('', autors,name="autors"),
    path('autors_create/', autors_create, name='autors_create'),
    path('book', books, name='book'),
    path('book_create/', book_create, name='book_create'),
    path('book_details/<int:id>/', details, name='details'),
    path('book_update/<int:id>/', book_update, name='book_update'),
]

from django.shortcuts import render,redirect
from .models import *

def autors(request):
    autors = Autor.objects.all()
    return render(request, 'autor.html', {'autors': autors})


def autors_create(request):
    if request.method == 'POST':
        Autor.objects.create(
            firstn =request.POST.get('firstn'),
            lastn =request.POST.get('lastn'),
            birth_d =request.POST.get('birth_d')
        )
        return redirect('autors')
    return render(request, 'autor_create.html')




def books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})



def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            Autor=request.POST.get('Autor'),
            pages=request.POST.get('pages'),
            price=request.POST.get('price'),
            desc=request.POST.get('desc')
        )
        return redirect('books')
    return render(request, 'book_create.html')




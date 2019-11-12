from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)#Show 10 units per page
    page = request.GET.get('page')
    filtered_books = paginator.get_page(page)
    return render(request, 'book_list.html',{ 'filtered_books' : filtered_books })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm
# Create your views here.

# making a default page
def home(request):
    context={}
    return render(request, 'myApp/base.html', context)

def landing(request):
    return render(request, 'myApp/landing.html')
# view book list
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myApp/book_list.html', {'books': books})

# create new books
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myApp/book_form.html', {'form': form})

# edit books
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'myApp/book_form.html', {'form': form})

#delete books
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'myApp/book_confirm_delete.html', {'book': book})

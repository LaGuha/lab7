from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.views.generic import View


class BookListView(View):

    def get(self, *args, **kwargs):
        books = Book.objects.all()
        return render(self.request,'lab/main.html',{'lane':books})

# Create your views here.
def main(request):
	lane=Book.objects.all()
	return render(request,'lab/main.html',{'lane':lane})
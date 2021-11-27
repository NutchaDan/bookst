from django.http import HttpResponse
from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.book_text for q in latest_book_list])
    return HttpResponse(output)

def detail(request, book_id):
    return HttpResponse("You're looking at question %s." % book_id)


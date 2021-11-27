from django.http import HttpResponse
from django.template import loader

from .models import Book


def index(request):
    latest_question_list = Book.objects.order_by('-pub_date')[:5]
    template = loader.get_template('database/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)

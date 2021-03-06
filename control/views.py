from rest_framework import viewsets
from control.serializers import ControlSerializer
from control.models import Control

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.response import Http404

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

class ControlViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list and retrieve actions.
    """
    queryset = Control.objects.all()
    serializer_class = ControlSerializer

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        search_post = request.GET.get('_book_text')
        if search_post or search_post == '':
            try:
                dataSet = self.queryset.filter(Q(book_text__icontains=search_post))
            except Control.DoesNotExist:
                raise Http404("Books does not exist")
        else:
            dataSet = self.queryset.all()
        books = self.serializer_class(dataSet, many=True)
        return Response(books.data)

@csrf_exempt
def bookApi(request,id=0):
    if request.method=='GET':
        books = Control.objects.all()
        Book_serializer = ControlSerializer(books, many=True)
        return JsonResponse(Book_serializer.data, safe=False)

    elif request.method=='POST':
        book_data=JSONParser().parse(request)
        book_serializer = ControlSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        book_data = JSONParser().parse(request)
        book=Control.objects.get(id=book_data['id'])
        book_serializer=ControlSerializer(book,data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        book=Control.objects.get(id=id)
        book.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
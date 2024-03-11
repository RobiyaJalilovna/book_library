from rest_framework.generics import ListAPIView

from book.models import Book
from .serializers import BookSerializer

# Create your views here.
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




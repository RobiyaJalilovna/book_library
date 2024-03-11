from django.views.generic import ListView
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list_html'


from rest_framework.authtoken.views import ObtainAuthToken


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


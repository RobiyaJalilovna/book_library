from django.urls import path
from .views import BookAPIView,CustomAuthToken

urlpatterns = [
    path('',BookAPIView.as_view()),
    path('api/token/', CustomAuthToken.as_view(), name='token_obtain_pair'),
]
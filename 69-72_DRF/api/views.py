from rest_framework import generics
from .serializers import QuoteSerializer

from quotes.models import Quote
from .permissions import IsOwnerOrReadOnly


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwnerOrReadOnly
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
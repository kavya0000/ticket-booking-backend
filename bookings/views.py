

from rest_framework import viewsets, filters
from .models import Ticket, Movie
from .serializers import TicketSerializer, MovieSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'event_name']

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')  # or '-created_at' if you have that field
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


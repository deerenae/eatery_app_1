from rest_framework import viewsets, permissions 
from eatery_backend.models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RestaurantSerializer
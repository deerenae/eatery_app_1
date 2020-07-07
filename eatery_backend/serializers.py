from rest_framework import serializers
from eatery_backend.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Restaurant
        fields = '__all__'
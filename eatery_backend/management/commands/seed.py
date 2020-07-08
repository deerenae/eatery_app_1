from django.core.management.base import BaseCommand
import requests
from ...models import Restaurant

# original_url = 'https://api.yelp.com/v3/businesses/search?term=restaurants&location=denver'

class Command(BaseCommand):
    def handle(self, *args, **options):
        get_restaurants()
        seed_restaurants()
        print('completed')



def get_restaurants():
        url = 'https://developers.zomato.com/api/v2.1/search?count=50&lat=39.7294&lon=-104.8319'
        r = requests.get(url, headers={'Content-Type': 'application/json', 
        'user-key': 'd8d852fde798a83350d11b5e17798c12'})
        restaurant= r.json()
        return restaurant['restaurants']

def seed_restaurants():
        for i in get_restaurants():
            restaurant= Restaurant(
                name=i['restaurant']['name'],
                address=i['restaurant']['location']['address'],
                thumb=i['restaurant']['thumb'],
                url=i['restaurant']['url'],
                menu_url=i['restaurant']['menu_url'],
                phone_numbers=i['restaurant']['phone_numbers'],
                has_table_booking=i['restaurant']['has_table_booking'],
                has_online_delivery=i['restaurant']['has_online_delivery']

            )
            restaurant.save()

def clear_data():
  Restaurant.objects.all().delete()
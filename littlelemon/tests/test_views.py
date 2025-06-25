from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemsViews(TestCase):
    def setUp(self):
        Bruschetta = MenuItem.objects.create(title='Bruschetta', price=8.50, inventory=10)
        Pasta = MenuItem.objects.create(title='Pasta', price=5.00, inventory=20)
    
    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bruschetta')
        self.assertContains(response, 'Pasta')
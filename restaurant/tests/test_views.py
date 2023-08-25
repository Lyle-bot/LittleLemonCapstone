from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.salad = MenuItem.objects.create(title='Salad', price=20, inventory=10)
        self.hotdog = MenuItem.objects.create(title='Hotdog', price=15, inventory=20)
        self.pasta = MenuItem.objects.create(title='Pasta', price=25, inventory=5)

    def test_getall(self):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        
        expected_data = [
            {'id': self.salad.id, 'title': 'Salad', 'price': '20.00', 'inventory': 10},
            {'id': self.hotdog.id, 'title': 'Hotdog', 'price': '15.00', 'inventory': 20},
            {'id': self.pasta.id, 'title': 'Pasta', 'price': '25.00', 'inventory': 5}
        ]

        self.assertEqual(serializer.data, expected_data)

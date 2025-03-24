from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def instance_menu (self):
        item=Menu.objects.create(f_name="IceCream", f_price=14,inventory=20)
        self.assertEqual(item,"IceCream : 20")

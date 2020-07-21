from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Done false ya hear, done false!')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Mind you, return ya self ya hear?!')
        self.assertEqual(str(item), 'Mind you, return ya self ya hear?!')

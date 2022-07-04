from django.test import TestCase
from django.urls import resolve
from myApp.views import website1_view
from django.http import HttpRequest
from .models import Item

# Create your tests here.

class HomepageTest(TestCase):

    def test_mainpage_equal_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'website1.html')

class CreateListTest(TestCase):

    def test_save_POST_request(self):
        response = self.client.post('/myApp/newlist_url/', {'entered_name': 'Silver'})
        self.assertEqual(Item.objects.count(), 1)
        newData = Item.objects.first()
        self.assertEqual(newData.name, 'Silver')

    def test_POST_redirect(self):
        response = self.client.post('/myApp/newlist_url/', {'entered_name': 'Adore'})
        self.assertRedirects(response, '/myApp/viewlist_url/')


class ViewTest(TestCase):
    def test_displays_all(self):
        Item.objects.create(name='Salvador')
        Item.objects.create(name='Silverio')

        response = self.client.get('/myApp/viewlist_url/')

        self.assertContains(response, 'Salvador')
        self.assertContains(response, 'Silverio')

    def test_listview_uses_listpage(self):
        response = self.client.get('/myApp/viewlist_url/')
        self.assertTemplateUsed(response, 'listpage.html')


class ORMTEST(TestCase):
    def test_saving_retriv(self):
        
        txtItem1 = Item()
        txtItem1.name = 'Item One'
        txtItem1.save()

        txtItem2 = Item()
        txtItem2.name = 'Item Two'
        txtItem2.save()

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)

        items1 = items[0]
        items2 = items[1]

        self.assertEqual(items1.name, 'Item One')
        self.assertEqual(items2.name, 'Item Two')

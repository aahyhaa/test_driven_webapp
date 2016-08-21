from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
# Create your tests here.
''' class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,3)
'''
class ListViewTest(TestCase):
    def test_displays_only_items_for_that_list(self):
	current_list=List.objects.create()
	Item.objects.create(text='itemey 1',list=current_list)
	Item.objects.create(text='itemey 2',list=current_list)
	other_list=List.objects.create()
	Item.objects.create(text='other list item1',list=other_list)
	Item.objects.create(text='other list itme2',list=other_list)
	response=self.client.get('/lists/%d/'% current_list.id)
	self.assertContains(response,'itemey 1')
	self.assertContains(response,'itemey 2')
	self.assertNotContains(response,'other list item1')
	self.assertNotContains(response,'other list item2')
    def test_uses_list_template(self):
	list_=List.objects.create()
	response=self.client.get('/lists/%d/'% list_.id)
	self.assertTemplateUsed(response,'list.html')
    def test_passes_correct_list_to_template(self):
	current_list=List.objects.create()
	other_list=List.objects.create()	
	response=self.client.get('/lists/%d/'% current_list.id)
	self.assertEqual(response.context['list'],current_list)
class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
	self.client.post('/lists/new',data={'item_text':'A new list item'})
	self.assertEqual(Item.objects.count(),1)
	new_item=Item.objects.first()
	self.assertEqual(new_item.text,'A new list item')
    def test_redirects_after_POST(self):
	response=self.client.post('/lists/new',data={'item_text':'A new list item'})
	list_=List.objects.first()
	self.assertRedirects(response,'/lists/%d/' % (list_.id,))
class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
	current_list=List.objects.create()
	other_list=List.objects.create()
    	self.client.post('/lists/%d/add_item'%(current_list.id,),data={'item_text':'A new item for an existing list'})
	self.assertEqual(Item.objects.count(),1)
	new_item=Item.objects.first()
	self.assertEqual(new_item.text,'A new item for an existing list')
	self.assertEqual(current_list,new_item.list)
    def test_redirects_to_list_view(self):
	other_list=List.objects.create()
	current_list=List.objects.create()
	response=self.client.post('/lists/%d/add_item' % (current_list.id),data={'item_text':'A new item for an existing list'})		
	self.assertRedirects(response,'/lists/%d/'%(current_list.id))
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
	self.assertEqual(found.func,home_page)
    def test_home_page_returns_correct_html(self):
	request=HttpRequest()
	response=home_page(request)
	#print repr(response.content)
	#print response.content
	self.assertTrue(response.content.startswith('<!DOCTYPE html>'))
	self.assertIn('<title>To-Do lists</title>',response.content)
	self.assertTrue(response.content.strip().endswith('</html>'))	
	expected_html=render_to_string('home.html')
	self.assertEqual(response.content,expected_html)

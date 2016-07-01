from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.
''' class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,3)
'''
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
	self.assertEqual(found.func,home_page)
    def test_home_page_returns_correct_html(self):
	request=HttpRequest()
	response=home_page(request)
	#print repr(response.content)
	print response.content
	self.assertTrue(response.content.startswith('<html>'))
	self.assertIn('<title>To-Do lists</title>',response.content)
	self.assertTrue(response.content.strip().endswith('</html>'))	
	expected_html=render_to_string('home.html')
	self.assertEqual(response.content,expected_html)

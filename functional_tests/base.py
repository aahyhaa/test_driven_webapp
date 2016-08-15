from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
'''
The name of the class should be StaticLiveServerTestCase.
It is renamed just before the 1.7 release.
I think the book is based on the beta version of Django 1.7. 
UPDATE  Make sure import it:  from django.contrib.staticfiles.testing import StaticLiveServerTestCase
'''
import unittest
import sys
class FunctionalTest(StaticLiveServerTestCase,unittest.TestCase):
    @classmethod
    def setUpClass(cls):
	for arg in sys.argv:
	    if 'liveserver' in arg:
	        cls.server_url='http://'+arg.split('=')[1]
		return
	super(StaticLiveServerTestCase,cls).setUpClass()
        cls.server_url=cls.live_server_url
    @classmethod
    def tearDownClass(cls):
	if cls.server_url==cls.live_server_url:
	    super(StaticLiveServerTestCase,cls).tearDownClass()
    def setUp(self):
        self.browser=webdriver.Chrome()
    def tearDown(self):
	self.browser.refresh()
	self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
	table=self.browser.find_element_by_id('id_list_table')
	rows=self.browser.find_elements_by_tag_name('tr')
	self.assertIn(row_text,[row.text for row in rows])

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
'''
The name of the class should be StaticLiveServerTestCase.
It is renamed just before the 1.7 release.
I think the book is based on the beta version of Django 1.7. 
UPDATE  Make sure import it:  from django.contrib.staticfiles.testing import StaticLiveServerTestCase
'''
from django.test import LiveServerTestCase
import time
import unittest
class NewVisitorTest(StaticLiveServerTestCase,unittest.TestCase):
    def test_layout_and_styling(self):
	self.browser.get(self.live_server_url)
	self.browser.set_window_size(1024,768)
	inputbox=self.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('testing\n')
	inputbox=self.browser.find_element_by_id('id_new_item')
	self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=10)
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(15)
	#self.live_server_url='http://localhost:8000/'
    def tearDown(self):
	self.browser.refresh()
	self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
	table=self.browser.find_element_by_id('id_list_table')
	rows=self.browser.find_elements_by_tag_name('tr')
	self.assertIn(row_text,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
	self.browser.get(self.live_server_url)
	self.assertIn('To-Do',self.browser.title)
	header_text=self.browser.find_element_by_tag_name('h1').text
	self.assertIn('To-Do',header_text)
	inputbox=self.browser.find_element_by_id('id_new_item')
	self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
	inputbox.send_keys('Buy peacock feathers')
	inputbox.send_keys(Keys.ENTER)
	edith_list_url=self.browser.current_url
	#time.sleep(10)
	self.assertRegexpMatches(edith_list_url,'/lists/.+')
	self.check_for_row_in_list_table('1: Buy peacock feathers')
	inputbox=self.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('Use peacock feathers to make a fly')
	inputbox.send_keys(Keys.ENTER)
	self.check_for_row_in_list_table('1: Buy peacock feathers')
	self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
	self.browser.quit()
	self.browser=webdriver.Chrome()
	self.browser.get(self.live_server_url)
	page_text=self.browser.find_element_by_tag_name('body').text
	self.assertNotIn('Buy peacock feathers',page_text)
	self.assertNotIn('make a fly',page_text)
	inputbox=self.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('Buy milk')
	inputbox.send_keys(Keys.ENTER)
	francis_lists_url=self.browser.current_url
	self.assertRegexpMatches(francis_lists_url,'/lists/.+')
	self.assertNotEqual(francis_lists_url,edith_list_url)
	page_text=self.browser.find_element_by_tag_name('body').text
	self.assertNotIn('Buy peacock feathers',page_text)
	self.assertIn('Buy milk',page_text)
	#self.fail('Finish the test!')



from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
	self.browser.get(self.server_url)
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
	self.browser.get(self.server_url)
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

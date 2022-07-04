import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# def tearDown(self):
	# 	self.browser.quit()

	def test_FindPC_DataEntry_Intel_AMD_SSD_HDD(self):

		self.browser.get(self.live_server_url)

		#variables
		username = self.browser.find_element_by_id('user')
		budget_box = self.browser.find_element_by_id('budget')
		intel_processor = self.browser.find_element_by_id('intel')
		processor_dropdown_list = self.browser.find_element_by_id('processor')
		motherboard_dropdown_list = self.browser.find_element_by_id('motherboardChoices')
		ssd_checkbox = self.browser.find_element_by_id('ssd')
		storageSize_dropdown_list = self.browser.find_element_by_id('size-storage-choice')
		ram_dropdown_list = self.browser.find_element_by_id('rams')
		graphicsCard_dropdown_list = self.browser.find_element_by_id('graphics-card')
		powerSupply_dropdown_list = self.browser.find_element_by_id('powersupplyChoices')
		chassis_dropdown_list = self.browser.find_element_by_id('pc_case_choice')
		fan_dropdown_list = self.browser.find_element_by_id('fan_choice')
		submit_button = self.browser.find_element_by_id('submit_button')
		
		#SelectVar
		selectProcessor = Select(processor_dropdown_list)
		selectMotherboard = Select(motherboard_dropdown_list)
		selectStorage = Select(storageSize_dropdown_list)
		selectRam = Select(ram_dropdown_list)
		selectGCard = Select(graphicsCard_dropdown_list)
		selectPSupply = Select(powerSupply_dropdown_list)
		selectChassis = Select(chassis_dropdown_list)
		selectFan = Select(fan_dropdown_list)

		#Automation
		username.click()
		username.send_keys('Silver Ganadores')
		budget_box.click()
		budget_box.send_keys(25000)
		intel_processor.click()

		#Selecting drop box
		selectProcessor.select_by_visible_text('Intel Core i5-3450')
		selectMotherboard.select_by_visible_text('Gigabyte GA-H61M-DS2')
		ssd_checkbox.click()
		selectStorage.select_by_visible_text('Kingspec -- 120gb')
		selectRam.select_by_visible_text('4GB Kingston HyperX Fury DDR4 2400Mhz')
		selectGCard.select_by_visible_text('Colorful GT1030 -- 2gb')
		selectPSupply.select_by_visible_text('InPlay GS450P -- 450Watts')
		selectChassis.select_by_visible_text('Keytech Arrow -- Mid Tower')
		selectFan.select_by_visible_text('Allan 12V Fan -- 80mm')
		submit_button.click()

		inputs = ['Intel Core i5-3450', 'Gigabyte GA-H61M-DS2'
		, 'Kingspec -- 120gb', '4GB Kingston HyperX Fury DDR4 2400Mhz',
		'Colorful GT1030 -- 2gb', 'InPlay GS450P -- 450Watts',
		'Keytech Arrow -- Mid Tower', 'Allan 12V Fan -- 80mm']

		table = self.browser.find_element_by_id('customers')

		for elements in inputs:
			self.assertIn(elements, table.text)

		time.sleep(1)

		addbuild = self.browser.find_element_by_id('addbuild')
		addbuild.click()
		
		budget_box = self.browser.find_element_by_id('budget')
		intel_processor = self.browser.find_element_by_id('intel')
		processor_dropdown_list = self.browser.find_element_by_id('processor')
		motherboard_dropdown_list = self.browser.find_element_by_id('motherboardChoices')
		ssd_checkbox = self.browser.find_element_by_id('ssd')
		storageSize_dropdown_list = self.browser.find_element_by_id('size-storage-choice')
		ram_dropdown_list = self.browser.find_element_by_id('rams')
		graphicsCard_dropdown_list = self.browser.find_element_by_id('graphics-card')
		powerSupply_dropdown_list = self.browser.find_element_by_id('powersupplyChoices')
		chassis_dropdown_list = self.browser.find_element_by_id('pc_case_choice')
		fan_dropdown_list = self.browser.find_element_by_id('fan_choice')
		submit_button = self.browser.find_element_by_id('submit_button')

		#SelectVar
		selectProcessor = Select(processor_dropdown_list)
		selectMotherboard = Select(motherboard_dropdown_list)
		selectStorage = Select(storageSize_dropdown_list)
		selectRam = Select(ram_dropdown_list)
		selectGCard = Select(graphicsCard_dropdown_list)
		selectPSupply = Select(powerSupply_dropdown_list)
		selectChassis = Select(chassis_dropdown_list)
		selectFan = Select(fan_dropdown_list)


		budget_box.click()
		budget_box.send_keys(99999)
		intel_processor.click()

		#Selecting drop box
		selectProcessor.select_by_visible_text('Intel Core i5-3450')
		selectMotherboard.select_by_visible_text('Gigabyte GA-H61M-DS2')
		ssd_checkbox.click()
		selectStorage.select_by_visible_text('Kingspec -- 120gb')
		selectRam.select_by_visible_text('4GB Kingston HyperX Fury DDR4 2400Mhz')
		selectGCard.select_by_visible_text('Colorful GT1030 -- 2gb')
		selectPSupply.select_by_visible_text('InPlay GS450P -- 450Watts')
		selectChassis.select_by_visible_text('Keytech Arrow -- Mid Tower')
		selectFan.select_by_visible_text('Allan 12V Fan -- 80mm')
		submit_button.click()

		inputs = ['Intel Core i5-3450', 'Gigabyte GA-H61M-DS2'
		, 'Kingspec -- 120gb', '4GB Kingston HyperX Fury DDR4 2400Mhz',
		'Colorful GT1030 -- 2gb', 'InPlay GS450P -- 450Watts',
		'Keytech Arrow -- Mid Tower', 'Allan 12V Fan -- 80mm']

		table = self.browser.find_element_by_id('customers')

		for elements in inputs:
			self.assertIn(elements, table.text)

# if __name__ == '__main__':
# 	unittest.main(warnings = 'ignore')
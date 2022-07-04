import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    # def tearDown(self):
    #     self.browser.quit()

    def test_app_and_review(self):
        self.browser.get(self.live_server_url)
        viewlist_url = self.browser.current_url
        input_box_name = self.browser.find_element_by_id('name1') 
        submit_butt = self.browser.find_element_by_id('name_submit')
        input_box_name.click()
        input_box_name.send_keys('Silver Ganadores')

        submit_butt.click()
    
        table = self.browser.find_element_by_id('table1')
        rows = table.find_elements_by_tag_name('tr')
        body = self.browser.find_element_by_tag_name('body').text


#to be continue
        self.assertIn('1: Silver Ganadores', [row.text for row in rows])
        viewlist_url2 = self.browser.current_url
        self.assertRegex(viewlist_url2, '/myApp/.+')
        self.assertNotEqual(viewlist_url, viewlist_url2)
        self.assertNotIn('Adore Ganadores', body)

        print(viewlist_url)
        print(viewlist_url2)


#     def test_app_and_review11(self):
#         self.browser.get(self.live_server_url)
#         # viewlist_url = self.browser.current_url
#         input_box_name = self.browser.find_element_by_id('name1') 
#         submit_butt = self.browser.find_element_by_id('name_submit')
#         input_box_name.click()
#         input_box_name.send_keys('Silver Ganadores')

#         submit_butt.click()
    
#         table = self.browser.find_element_by_id('table1')
#         rows = table.find_elements_by_tag_name('tr')
#         body = self.browser.find_element_by_tag_name('body').text


# #to be continue
#         self.assertIn('1: Silver Ganadores', [row.text for row in rows])
#         viewlist_url = self.browser.current_url
#         self.assertRegex(viewlist_url, '/myApp/.+')
#         # self.assertNotEqual(viewlist_url, viewlist_url2)
#         # self.assertNotIn('Adore Ganadores', body)

#         # print(viewlist_url)
#         # print(viewlist_url2)

#         self.browser.quit()
        
#         self.browser = webdriver.Firefox()
#         self.browser.get(self.live_server_url)
#         input_box_name = self.browser.find_element_by_id('name1') 
#         submit_butt = self.browser.find_element_by_id('name_submit')
#         input_box_name.click()
#         input_box_name.send_keys('Adore Ganadores')

#         submit_butt.click()
    
#         table = self.browser.find_element_by_id('table1')
#         rows = table.find_elements_by_tag_name('tr')
#         body = self.browser.find_element_by_tag_name('body').text


# #to be continue
#         self.assertIn('2: Adore Ganadores', [row.text for row in rows])
#         viewlist_url2 = self.browser.current_url
#         self.assertRegex(viewlist_url2, '/myApp/.+')
#         self.assertNotEqual(viewlist_url, viewlist_url2)
#         self.assertIn('Silver Ganadores', body)
#         self.assertIn('Adore Ganadores', body)


#     def test_app_and_review_other_url(self):
#         self.browser.get(self.live_server_url)
#         input_box_name = self.browser.find_element_by_id('name1') 
#         submit_butt = self.browser.find_element_by_id('name_submit')
#         input_box_name.click()
#         input_box_name.send_keys('Adore Ganadores')

#         submit_butt.click()

#         self.browser.get(self.live_server_url)
#         input_box_name = self.browser.find_element_by_id('name1') 
#         submit_butt = self.browser.find_element_by_id('name_submit')
#         input_box_name.click()
#         input_box_name.send_keys('Salvador Ganadores')
#         submit_butt.click()
        
#         table = self.browser.find_element_by_id('table1')
#         rows = table.find_elements_by_tag_name('tr')
#         self.assertIn('1: Adore Ganadores', [row.text for row in rows])
#         self.assertIn('2: Salvador Ganadores', [row.text for row in rows])

# #to be continue
#         viewlist_url = self.browser.current_url
#         self.assertRegex(viewlist_url, '/myApp/.+')
    


# if __name__ == '__main__':
#     unittest.main(warnings='ignore') 
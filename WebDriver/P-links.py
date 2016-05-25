# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Persian Department" : "De Anza College :: Persian :: Home",
            "Philosophy Department" : "De Anza College :: Philosophy :: Home",
            "Phone Numbers, Frequently Needed" : "De Anza College :: Directories :: Frequently Needed Phone Numbers",
            #Photo ID: see
            "DASB Card" : "De Anza College :: DASB Card :: Home",
            "Photography Department" : "The De Anza College Photography Department",
            "Physical Education" : "De Anza College :: Physical Education :: Home",
            "Physical Education and Athletics Division" : "De Anza College :: Physical Education and Athletics :: Home",
            "Physical Science, Mathematics, and Engineering" : "De Anza College :: PSME :: Home"
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

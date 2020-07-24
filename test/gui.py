from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback
import sys

browser = webdriver.Firefox()
theException = BaseException

try:
      browser.get("http://www.michaelslab.net")
      assert browser.title == "About - Michaelslab"

      search = browser.find_element_by_class_name('search-words')
      search.send_keys("Ada")
      submit = browser.find_element_by_class_name('search-submit')
      submit.click()

      search_result = browser.find_elements_by_class_name( "search-entry-title")

      for i in range(len(search_result)):
          result = search_result[i];
          print( result.get_attribute("innerHTML") )



except Exception as theException :
      print("**** exception ")
      print(type(theException), theException.args)
      tb = sys.exc_traceback; 
      traceback.print_tb(tb)
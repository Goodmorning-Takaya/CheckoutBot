from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import urllib.request
import os
from configparser import ConfigParser
import tkinter as tk

#TEST ITEM

nikeURL = 'https://www.nike.com/t/mens-basketball-t-shirt-RxlfV9/DV1214-100'
colorBTNclass = 'nr-pdp-colorway-DV1214-100'
sizeBTNid = 'skuAndSize__27962581'
addCartBTNclass = 'ncss-btn-primary-dark btn-lg add-to-cart-btn'
driver = webdriver.Safari()
action = ActionChain(driver)

def setupConfig(file: str) -> ConfigParser:
	print("Parsing Configuration...")
	config = ConfigParser()
	config.read("file")
	return config

class CheckoutBot():
	'''Bot automates purchasing a product given a product URL, credentials and size/color'''
	def __init__(self,config, URL, size, color):
		self.username = config.get("NIKE_ACCOUNT", "USERNAME")
		self.password = config.get("NIKE_ACCOUNT", "PASSWORD")
		self.ID = config.get("NIKE_ACCOUNT", "ID")
		self.card = config.get("CREDIT_CARD", "CCNUM")
		self.ccsecurity = config.get("CREDIT_CARD", "CCV")
		self.expiration_month = config.get("CREDIT_CARD", "EXPM")
		self.expiration_year = config.get("CREDIT_CARD", "EXPY")
		self.URL = driver.get(nikeURL)
		self.addcartElement = driver.find_element(By.CLASS_NAME, addCartElem)
		self.colorElement = driver.find_element(By.CLASS_NAME, color)
		self.sizeElement = driver.find_element(By.ID, size)

	def login(self) -> None:
		'''Uses the webdriver to locate the login fields and logs the user in using the passed credentials'''
                signBTN = 'nav-btn p0-sm d-sm-b body-4 u-bold ml2-sm mr2-sm'
		logID = 'id="192ffd08-4d60-408c-8c75-821cad9c0cc7"'
		pwID = '3104580a-d23b-43d1-8782-babc5be49fad'
		

		signBTNclick = driver.find_element(BY.CLASS_NAME, signBTN)
		login = driver.find_element(By.THING, logID)
		pw = driver.find_element(By.THING, pwID)

		action.move_to_element(signBTNclick)
		action.click(signBTNclick)
		action.move_to_element(login)
		action.click(login)
		action.send_keys(username)
		action.move_to_element(pw)
		action.click(pw)
		action.send_keys(password)
		action.perform()
		pass

	def purchase(self) -> None:
		'''Execute a purchase'''
		pass

	def _selectColor(self) -> None:
		'''Uses the webdriver to select the color of item to be checked out'''
		action.move_to_element(colorElement)
		action.click(colorElement)
		pass

	def _selectSize(self) -> None:
		'''Uses the webdriver to select the size of item to be checked out'''
		driver.move_to_element(sizeElement)
		driver.click(sizeElement)
		pass

	def _addToCart(self) -> None:
		'''Uses the webdriver to create and execute an action chain to reach the checkout page'''
		action.move_to_element(addcartElement)
		action.click(addcartElement)
		pass

	def _checkout(self) -> None:
		'''Uses the webdriver to complete checkout of order'''
		checkoutCLASS = 'ncss-btn-primary-dark btn-lg mr3-sm css-1n4ymyz'
		checkoutBTN = driver.find_element(By.CLASS_NAME, checkoutCLASS)
		action.move_to_element(checkoutBTN)
		action.click(checkoutBTN)
                #IF Nike Account, all info should be filled, just need to click 'Place Order'
		placeorderID = ''
		placeorderBTN = driver.find_element(By.ID, placeorderID)
		action.move_to_element(placeorderBTN)
		action.click(placeorderBTN)
		pass
	    
        def _enterCard(self) -> None:
                '''If needed, uses webdriver to autofill card info'''
                
                
if __name__ == "__main___":
	config = setupConfig("config.ini")
	print("Launching Bot...")
	bot = CheckoutBot(config, nikeURL, sizeElem, colorElem)
	time.sleep(1)
	print("Logging in...")
	bot.login()
	print("Making purchase...")
	bot.purchase()
	print("Purchase complete!")

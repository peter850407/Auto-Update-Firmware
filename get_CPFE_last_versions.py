#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

import sys,time

# BOARD = ["brask", "brya" , "etc."]
# ImageType = ["FIRMWARE_IMAGE_ARCHIVE", "TEST_IMAGE_ARCHIVE", "etc."]
# Channel = ["beta", "canary", "dev", "stable"]

try:
	selectBoard = sys.argv[1]
	setVersion_prefix = sys.argv[2]
except IndexError as e:
	setVersion_prefix = ""
selectImageType = "FIRMWARE_IMAGE_ARCHIVE"
selectChannel = "dev"

print("Search \033[93m"
 + selectBoard + " "
 + selectImageType + " \""
 + selectChannel.upper() + " Channel\" "
 + setVersion_prefix + "\033[0m")

""" object of ChromeOptions class """
options = Options()

""" adding specific command """
options.add_argument("user-data-dir=./GoogleProfile")	# Local Chrome Profile Path
options.add_argument("headless")		# Hide browser
options.add_argument("disable-gpu")		# Disable gpu to avoid Mesa-library
# options.add_argument("remote-debugging-port=9222")
options.add_argument("enable-features=WebContentsForceDark")	# Dark mode
options.add_argument("blink-settings=imagesEnabled=false")	# Block image
# options.debugger_address='127.0.0.1:9222'
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# """
# 	With selenium4 as the key executable_path is deprecated.
# 	You have to use an instance of the Service().
# """
# # s = Service(".\chromedriver")

""" set chromedriver.exe path """
driver = webdriver.Chrome(options = options)
# driver = webdriver.Chrome(service = s, options = options)

# """ minimize browser """
# driver.minimize_window()

# """ change browser window size """
# driver.set_window_size(500, 500)

# """ set window position """
# driver.set_window_position(0, 0, windowHandle ='current')

################################################################################
#                                     MAIN                                     #
################################################################################

# driver.get("https://www.google.com/chromeos/partner/fe/#release")
driver.get("https://www.google.com/chromeos/partner/fe/#release:board="
 + selectBoard
 + "&channel=" + selectChannel
 + "&type=" + selectImageType
 + "&ver=" + setVersion_prefix)
print("Now Loading... Now Loading... Now Loading...")

# time.sleep(3)
# Board = driver.find_element(By.XPATH, "(//select[@class='NCY5R1C-H-g'])[1]")
# Select(Board).select_by_value(selectBoard)

# Image_Type = driver.find_element(By.XPATH, "(//select[@class='NCY5R1C-H-g'])[2]")
# Select(Image_Type).select_by_value(selectImageType)

# Channel = driver.find_element(By.XPATH, "(//select[@class='NCY5R1C-H-g'])[3]")
# Select(Channel).select_by_value(selectChannel)

# Version_prefix = driver.find_element(By.XPATH, "(//input[@type='text'][@class='NCY5R1C-H-h'])[2]")
# Version_prefix.send_keys(setVersion_prefix)

# Search = driver.find_element(By.CLASS_NAME, "NCY5R1C-H-c")
# Search.click()


# # time.sleep(5)
driver.implicitly_wait(6)
# Version = driver.find_elements(By.XPATH, "(//td[contains(@class, 'NCY5R1C-d-d')])")
Version = driver.find_elements(By.CLASS_NAME, "NCY5R1C-d-d")
Next_page = driver.find_element(By.XPATH, "(//img[@class='gwt-Image'][@role='button'])[3]")

Item = driver.find_element(By.CLASS_NAME, "gwt-HTML")
Item = Item.text.split("of")			# split by "of"  Ex. 1-20 of 1,968
AllItem = Item[1].replace(",","")		# choose after "of" and
										# remove thousandth place  Ex. 1,968 -> 1968
""" No version founded """
if Version == []:
	print("\n\033[1;96mVersion\033[0m not found!\n")
	driver.quit()
	exit()

print("\n\033[1;96mVersion\033[0m")
print("\033[1;94mpage (1) -->")

num = 0
pretext = ""

for item in range(int(int(AllItem) / 20)):	# A page include 20 items
	divide = 0
	for i in Version:
		""" Avoid null row """
		if i.text == "":
			continue

		""" Avoid the same version """
		if pretext == i.text:
			continue
		pretext = i.text

		""" Print version every 5 items """
		num += 1
		divide += 1
		print ("{:<11} {:<20} ".format("".join(["\033[1;95m", str(num), "."]),
		"".join(["\033[0m\033[92m", pretext])), end=" ")
		# print ("{:<4} {:<20} ".format(str(num) + ".", "\033[0m\033[92m" + i.text), end=" ")
		if divide % 5 == 0:
			print()
	if divide % 5 != 0:
		print()
	print("".join(["\033[1;94mpage (", str(item + 2), ") -->"]))
	# print("\033[1;94mpage (" + str(item + 2) + ") -->")
	Version.clear()
	Next_page.click()
	driver.implicitly_wait(3)
	Version = driver.find_elements(By.CLASS_NAME, "NCY5R1C-d-d")
	# screenshot_path = '/home/peter/Downloads/Auto-Update-Firmware/screenshot.png'
	# driver.save_screenshot(screenshot_path)


""" Print last page """
Version.clear()
time.sleep(1)	# sleep 1 second to avoid change page error
Last_page = driver.find_element(By.XPATH, "(//img[@class='gwt-Image'][@role='button'])[4]")
Last_page.click()
# driver.implicitly_wait(3)
Version = driver.find_elements(By.CLASS_NAME, "NCY5R1C-d-d")

for i in Version:
		""" Avoid null row """
		if i.text == "":
			continue

		""" Avoid the same version """
		if pretext == i.text:
			continue
		pretext = i.text

		""" Print version every 5 items """
		num += 1
		print ("{:<11} {:<20} ".format("".join(["\033[1;95m", str(num), "."]),
		"".join(["\033[0m\033[92m", pretext])), end=" ")
		# print ("{:<4} {:<20} ".format(str(num) + ".", "\033[0m\033[92m" + i.text), end=" ")
		if num % 5 == 0:
			print()
print("\n")

""" close browser """
driver.quit()

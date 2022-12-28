from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

print("Default search \033[93m"
 + selectImageType + "\033[0m and \033[93m"
 + selectChannel.upper() + " Channel\033[0m")

""" object of ChromeOptions class """
options = Options()

""" adding specific command """
options.add_argument("user-data-dir=./GoogleProfile")    # Local Chrome Profile Path
options.add_argument("headless")    # Hide browser
options.add_argument("disable-gpu")    # Disable gpu to avoid Mesa-library
# options.add_argument("remote-debugging-port=9222")
options.add_argument("enable-features=WebContentsForceDark")    # Dark mode
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


# time.sleep(5)
driver.implicitly_wait(10)
# Version = driver.find_elements(By.XPATH, "(//td[contains(@class, 'NCY5R1C-d-d')])")
Version = driver.find_elements(By.CLASS_NAME, "NCY5R1C-d-d")

""" No version founded """
if Version == []:
	print("\n\033[96m\033[1mVersion\033[0m not found!\n")
	driver.quit()
	exit()

print("\n\033[96m\033[1mVersion\033[0m")

num = 0
for i in Version:
	""" Avoid null row """
	if i.text == "":
		continue

	""" Print version every 5 items """
	num += 1
	print("\033[95m\033[1m" + "%3s" % (str(num) + ".") + "\033[0m", end=" ")
	print("\033[92m" + i.text + "\033[0m", end="\t")
	if num % 5 == 0:
		print()
print("")

""" close browser """
driver.quit()

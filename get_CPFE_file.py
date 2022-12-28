from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service

import glob,os,sys,time

# BOARD = ["brask", "brya" , "etc."]
# ImageType = ["FIRMWARE_IMAGE_ARCHIVE", "TEST_IMAGE_ARCHIVE", "etc."]
# Channel = ["beta", "canary", "dev", "stable"]

try:
	selectBoard = sys.argv[1]
	selectImageType = sys.argv[2]
	selectChannel = sys.argv[3]
	setVersion_prefix = sys.argv[4]
except IndexError as e:
	print("You are first login!! After first login, Ctrl + C")
	print("You are first login!! After first login, Ctrl + C")
	print("You are first login!! After first login, Ctrl + C")

	time.sleep(1)
	options = Options()
	options.add_argument("user-data-dir=./GoogleProfile")    # Local Chrome Profile Path
	options.add_argument("enable-features=WebContentsForceDark")    # Dark mode
	driver = webdriver.Chrome(options = options)
	driver.get("https://accounts.google.com/")
	time.sleep(666)
	exit()

download_dir = os.path.abspath(os.getcwd())+"/CPFE_Downloads"

""" check file is already in storage """
if glob.glob(download_dir + "/ChromeOS-firmware-*" + setVersion_prefix + "*.tar.bz2"):
	print("File is in storage !!!")
	exit()


""" object of ChromeOptions class """
options = Options()


""" Download files to a specific folder in Chrome browser using Selenium """
options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False
})

""" adding specific command """
options.add_argument("user-data-dir=./GoogleProfile")    # Local Chrome Profile Path
# options.add_argument("headless")    # Hide browser
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

""" change browser window size """
driver.set_window_size(500, 500)

""" set window position """
driver.set_window_position(0, 0, windowHandle ='current')

################################################################################
#                                     MAIN                                     #
################################################################################

""" launch URL """
# driver.get("https://www.google.com/chromeos/partner/fe/#release")
driver.get("https://www.google.com/chromeos/partner/fe/image_download?board="
 + selectBoard
 + "&type=" + selectImageType
 + "&channel=" + selectChannel
 + "&version=" + setVersion_prefix)

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

# time.sleep(3)

# Filename = driver.find_element(By.XPATH, "(//a[@class='gwt-Anchor'])")
# Filename.click()

print("Now Loading... Now Loading... Now Loading...")

try:
	""" Not Found  Error 404 """
	if driver.find_element(By.TAG_NAME, "h1").text == "Not Found":
		print("\nFile Not Found!!! Please check version and try again!")
		driver.quit()
		exit(1)
except Exception as exception:
	# min = -0.5
	# while not glob.glob(download_dir + "/ChromeOS-firmware-*" + setVersion_prefix + "*.tar.bz2"):
	# 	min += 0.5
	# 	print("File download is not completed ... (" + str(min) + " min)")
	# 	time.sleep(30)
	# print("\nFile download is completed !!!     (" + str(min + 0.5) + " min)\n")
	shadow_content = " "

	driver.get("chrome://downloads/")
	driver.minimize_window()
	print()
	while shadow_content != "":
		time.sleep(0.5)

		shadow_host1 = driver.find_element(By.TAG_NAME, "downloads-manager")
		shadow_root1 = shadow_host1.shadow_root

		mainContainer = shadow_root1.find_element(By.ID, "mainContainer")

		shadow_host2 = mainContainer.find_element(By.TAG_NAME, "downloads-item")
		shadow_root2 = shadow_host2.shadow_root

		shadow_content = shadow_root2.find_element(By.ID, "description").text

		print(shadow_content, end="\r")

	os.system("notify-send 'File Download Finished!'")
	print("\nFile Download Finished!!\n")

	""" close browser """
	driver.quit()

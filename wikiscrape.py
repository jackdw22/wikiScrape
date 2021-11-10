import requests
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from os import chdir # for writing to a specified save folder
import time
from selenium import webdriver
import keyboard
from func_timeout import func_timeout, FunctionTimedOut

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r'R:\JoePriceResearch\school_menus\school_menu_scrapes\chromedriver2.exe')
driver.get('https://en.wikipedia.org/w/index.php?search=+&title=Special%3ASearch&go=Go&ns0=1')
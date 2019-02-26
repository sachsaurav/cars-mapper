from bs4 import BeautifulSoup
import os
import requests
import csv
from selenium import webdriver
import time
import json 
# import docx
import xlwt
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from xlrd import open_workbook


driver = webdriver.Chrome(executable_path = r'D:\chrome driver\chromedriver.exe')
# driver.get('https://www.edmunds.com/finder/car-finder-results.html#!new/year%3A2019/baseMsrp%3Aasc/15')
# time.sleep(3)
urls=[]
wb = open_workbook(r'D:\office docs\2019_edmunds data\crawled dec end\edmunds available cars.xlsx')
for s in wb.sheets():
	count=0
	for i in range(0,s.nrows):
		urls.append(str(s.cell(i,2).value))
print(len(urls))
# print(urls)
urls=urls[1:]
table_heads=[]
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("edmunds trim ids")
r=0
for url in urls:
	try:	
		print(url)
		driver.get(url)
		# table=driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/table')
		# # print(table.text)
		# table_name=driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/table/thead/tr/th[1]')
		# print("table-name= "+table_name.text)
		# element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/table/thead/tr/th[2]/select')
		# all_options = element.find_elements_by_tag_name('option')
		# print(len(all_options))
		# trims=Select(driver.find_element_by_css_selector('.custom-select.mb-1_25.medium.font-weight-bold.w-100'))
		# # for option in all_options:
		# # 	print("Value is: %s" % option.get_attribute('value'))
		# # 	element.select_by_value(option)
		# # 	time.sleep(2)
		# # for options in all_options:
		# # 	print(options)
		# # 	trims.select_by_value(option)
		el=driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/table/thead/tr/th[2]/select')
		c=1
		for option in el.find_elements_by_tag_name ('option'):
			r+=1
			sheet1.write(r,0,url)
			print(option.text)
			print(option.get_attribute('value'))
			sheet1.write(r,c+1,option.text)
			sheet1.write(r,c,option.get_attribute('value'))
		
			book.save('edmunds_trim_list_2019_12_28.xls')
	except Exception as e:
		print(e)
		driver.close()
		driver=webdriver.Chrome(executable_path = r'D:\chrome driver\chromedriver.exe')
		pass

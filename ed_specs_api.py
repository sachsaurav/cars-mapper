import requests
import json
import pandas
from xlrd import open_workbook
import xlwt
from selenium import webdriver
import time

# r=requests.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/401761711/features-specs')
wb = open_workbook(r'D:\office docs\2019_edmunds data\crawled dec end\edmunds_trim_list_2019_12_28.xls')
row=0
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("edmunds_data")
driver = webdriver.Chrome(executable_path = r'D:\chrome driver\chromedriver.exe')


lists=['401732422',
'401747430',
'401747436',
'401747437',
'401752350',
'401752351',
'401752352',
'401752353',
'401752354',
'401752355',
'401752356',
'401752357',
'401752522',
'401752523',
'401752524',
'401752525',
'401752526',
'401752527',
'401752528',
'401752529',
'401753961',
'401753962',
'401753963',
'401753964',
'401753965',
'401753966',
'401753967',
'401753968',
'401753969',
'401753970',
'401753971',
'401754548',
'401754549',
'401754550',
'401754600',
'401754602',
'401754739',
'401754742',
'401758433',
'401758434',
'401758435',
'401763604',
'401763605',
'401764370',
'401764371',
'401764372',
'401764373',
'401764374',
'401764375',
'401764376',
'401764377',
'401765005',
'401765007',
'401765008',
'401765009',
'401765017',
'401765018',
'401765019',
'401765021',
'401765023',
'401765025',
'401765109',
'401765111',
'401765112',
'401765113',
'401765114',
'401765115',
'401765116',
'401765118',
'401765126',
'401765127',
'401765129',
'401765130',
'401765132',
'401765133',
'401765135',
'401765136',
'401765137',
'401765138',
'401766884',
'401766885',
'401766886',
'401766887',
'401767037',
'401767038',
'401767039',
'401767040',
'401767041',
'401767042',
'401767043',
'401768563',
'401768568',
'401768631',
'401768635',
'401768640',
'401768641',
'401768643',
'401768646',
'401768648',
'401769016',
'401769017',
'401769020',
'401769021',
'401769061',
'401769062',
'401769063',
'401769064',
'401769065',
'401769066',
'401769067',
'401769068',
'401769069',
'401769070',
'401769071',
'401769072',
'401769073',
'401769077',
'401769083',
'401769087',
'401769092',
'401769416',
'401769417',
'401773160',
'401773161',
'401773164',
'401773165',
'401773166',
'401773167',
'401773466',
'401773467',
'401773469',
'401773470',
'401773623',
'401773624',
'401773626',
'401773627',
'401773893',
'401773894',
'401773895',
'401773896',
'401773897',
'401773898',
'401773899',
'401773900',
'401773901',
'401773902',
'401774702',
'401774703',
'401778012',
'401778013',
'401778014',
'401778015',
'401778016',
'401778017',
'401778018',
'401779429',
'401779430',
'401779431',
'401779432',
'401779436',
'401779437',
'401779438',
'401779439',
'401779752',
'401779753',
'401779754',
'401779755',
'401779756',
'401779757',
'401779758',
'401779759',
'401779760',
'401779761',
'401779762',
'401779763',
'401779764',
'401779765',
'401779766',
'401779767',
'401779768',
'401779769',
'401779770',
'401779771',
'401779772',
'401779773',
'401779774',
'401779775',
'401779776',
'401779777',
'401779778',
'401779779',
'401780276',
'401780277',
'401780278',
'401781618',
'401781828',
'401781829',
'401781830']
# for s in wb.sheets():
# 	count=0
# 	for i in range(2202,s.nrows):
# 		car=str(s.cell(i,0).value)
# 		if(len(str(s.cell(i,1).value))>1):
# 			trim=str(s.cell(i,1).value).strip()
# 			# r=requests.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/'+str(int(trim[:-2]))+'/features-specs')
# 			driver.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/'+str(int(trim[:-2]))+'/features-specs')
# 			time.sleep(3)
# 			html=driver.find_element_by_tag_name('body').text
# 			print(html)
# 			print(int(trim[:-2]))
# 			sheet1.write(row,0,car)
# 			sheet1.write(row,1,trim)
# 			sheet1.write(row,2,str(html))
# 			row+=1
# 		book.save("edmunds_2019_cars_data_4.xls")


for i in lists:
	car=i
	if(len(i)>1):
		trim=str(i).strip()
		# r=requests.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/'+str(int(trim[:-2]))+'/features-specs')
		driver.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/'+trim+'/features-specs')
		time.sleep(3)
		html=driver.find_element_by_tag_name('body').text
		print(html)
		print(int(trim))
		sheet1.write(row,0,car)
		sheet1.write(row,1,trim)
		sheet1.write(row,2,str(html))
		row+=1
	book.save("edmunds_2019_cars_data_5.xls")
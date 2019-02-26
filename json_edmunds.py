# import requests
import json
# import pandas
from xlrd import open_workbook
import xlwt


# r=requests.get('https://www.edmunds.com/gateway/api/vehicle/v4/styles/401761711/features-specs')
wb = open_workbook(r'C:\Users\CD User\Desktop\PYTHON PROGRAMS\edmunds_2019_cars_data.xls')

# c=c[1:-2]
heads_list=[]
lists=[]
for s in wb.sheets():
	for i in range(0,s.nrows):
		# print(s.cell(i,3).value)
		if(len(s.cell(i,2).value)>2):
			lists.append(str(s.cell(i,2).value))
# print(lists)
# lists.append(data)
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("edmunds crawled specs sheet")
sheet2 = book.add_sheet("edmunds uncrawled specs sheet")
r=0
row=0
for k,data in enumerate(lists):
	try:
		print(k)
		print('*********************')

		j=json.loads(data)
	except Exception as e:
		print("not loading")
		print(e)

		# print(data)
		data="\'"+data+"\'"
		# dataform = str(data).strip("'<>() ").replace('\'', '\"')
		# print(data)
		print(data)
		j=json.loads(data)
		# try:
		# 	j=json.loads(data[0])
		# except Exception as e:
		# 	j=json.loads(data[1])
		# 	pass
		sheet2.write(row,0,data)
		row+=1
		continue
	r+=1
	col=0
	for a,b in j.items():
		# print("super-heads",a)
		try:

			for c,d in b.items():
				print("heads-",c)
				print("values- ",d)
				if (c not in heads_list):
					heads_list.append(c)
				sheet1.write(r,col,(str(c)+"- "+str(d)))
				col+=1

				# print("values-", d)
				# try:
				# 	# print('items')
				# 	if c in d.items():
				# 		print("c")
				# except Exception as e:
				# 	print("no items ",d)
				# 	sheet1.write(r,col,(str(c)+"-  "+str(d)))
				# 	col+=1
				# 	pass
				try:
					for o,p in d.items():

						# print("next")
						print("sub-heads-",o)
						print("sub-values-",p)
					# 	# for k,l in p.items():
					# 	# 	print(k,l)
					print("next")
				except Exception as e:
					print(e)
					print("inner exception")
					print(c,d)
					pass
		except Exception as e:
			# print(e)
			print("1st exception")
			print(a,":",b)
			sheet1.write(r,col,(str(a)+"- "+str(b)))
			col+=1
			pass

print(heads_list)
book.save("trim_data_2019_2.xls")
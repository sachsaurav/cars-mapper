import pandas as pd
import xlrd
import xlwt

df=pd.read_excel(r'C:\Users\CD User\Desktop\carguruMapping\cargurus json parsed 17-18.xlsx', headers=False)

df2=pd.DataFrame()
row=1
for i in range(0,df.shape[0]):
	transmissions=[]
	engines=[]
	# print(df.iloc[i,24])
	data=df.iloc[i,24]
	for d in data.split('|'):
		# print(d)
		if ("speed" in d.lower()) or ("continuous" in d.lower()):
			transmissions.append(d)
			# print(d)
		if("hp" in d.lower()):
			engines.append(d)
			print(d)
	for e in engines:
		for t in transmissions:
			row+=1

			for j in range(0,24):
				df2.loc[row,j]=df.iloc[i,j]
			df2.loc[row,24]=e
			df2.loc[row,25]=t

			for j in range(25,df.shape[1]):
				df2.loc[row,j+1]=df.iloc[i,j]

			
	print(df.iloc[i,0])
	# print("engines")
	# for e in engines:
	# 	print(e)
	# print("transmissions")
	# for t in transmissions:
	# 	print(t)

df2.to_excel('carguru engine_transmission_separated.xlsx')


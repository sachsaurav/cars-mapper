import pandas as pd
import json
df=pd.read_excel(r'D:\CARHP\trim mapping\cargurus\18-17 cargurus.xlsx', headers=False)


df2=pd.DataFrame()
heads=[]
for i in range(1,df.shape[0]):
		# for j in range(1,df.shape[1]):
	c={}
	df2.loc[i,0]=df.iloc[i,0]
	print(df.iloc[i,0])
	print(df.iloc[i,1])
	# print(df.iloc[i,2])
	df2.loc[i,1]=df.iloc[i,1]
	# df2.loc[i,2]=df.iloc[i,2]
	# df2.loc[i,0]=df.iloc[i,0]
	c=df.iloc[i,2]
	data=json.loads(c)
	# print(data.keys())
	for key in data.keys():
		if str(key) in heads:
			pass
		else:
			print(key)
			heads.append(str(key))



	for k,v in data.items():
		df2.loc[i,(heads.index(str(k))+3)]=str(v)
		print((heads.index(str(k))+3))
		# df2.to_excel('cargurus json parsed.xlsx')

col=3
for h in heads:
	print(h)
	df2.loc[i+1,col]=str(h)
	col+=1

df2.to_excel('cargurus json parsed.xlsx')


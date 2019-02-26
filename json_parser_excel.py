import pandas as pd
import json
df=pd.read_excel(r'D:\CARHP\trim mapping\cargurus\18-17 cargurus.xlsx', headers=False)


df2=pd.DataFrame()
heads=[]
for i in range(2,df.shape[0]):
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
		if key not in heads:
			heads.append(key)



	for k,v in data.items():
		df.loc[i,(heads.index(k)+3)]=v

col=3
for h in heads:
	df.iloc[i+1,col]=h
	col+=1

df2.to_excel('cargurus json parsed.xlsx')


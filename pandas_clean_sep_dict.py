# import deps
import sys
import json
# import ast # handle single/double quote in dict/json string
import pandas as pd

print(f'Python  version: {sys.version}')
print(f'pandas version: {pd.__version__}')
print(pd.Timestamp.now())

# นำเข้าไฟล์ที่มี seperate เป็น tab ให้ใส่ parameter sep='\t' เพื่อระบุให้แบ่ง col ด้วย \t
df=pd.read_csv('https://github.com/prasertcbs/basic-dataset/raw/master/dict_list_column.tsv', sep='\t')
df

type(df['price'][0])

# แสดง ชื่อ col, type, example ข้อมูล
for c in df.columns:
    print(f'{c:10}: {type(df[c][0])} {df[c][0]}')

# ใช้ func loads จาก deps json เพิ่อทำการแปลงข้อมูลจาก str -> dict
j=json.loads('{"S":40, "M":50, "L":60}')
print(type(j))
print(j)

# ใช้ func map เพื่อนำ json.loads มาใช้กับข้อมูลใน col [price]
df['price_j']=df['price'].map(json.loads)
# df['price_j']=df['price'].apply(lambda s: json.loads(s))
df.head()

# แยก dict ออกไปเป็น col
df['price_small'] = df['price_j'].apply(lambda v: v['S'])
df['price_medium'] = df['price_j'].apply(lambda v: v['M'])
df['price_large'] = df['price_j'].apply(lambda v: v['L'])

df.head()

# export to excel or csv
# df.to_csv('price_coffee.csv',index=False)
# df.to_excel('price_coffee.xlsx', index=False)
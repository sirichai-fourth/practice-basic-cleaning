# import dependencies
import sys
import pandas as pd
import numpy as np

# pandas set display
pd.set_option('display.max_rows', None)

%config InlineBackend.figure_format='retina'

# print version
print(f'Python version:  {sys.version}')
print(f'pandas version:  {pd.__version__}')
pd.Timestamp.now()

## Read data from excel
df=pd.read_excel('https://github.com/prasertcbs/basic-dataset/raw/master/starbucks_bakery.xlsx')
df.head(20)


## Drop blank row
# ข้อมูลใน row ที่เป็น Null ทั้งหมดถูกลบออกไป แต่ index ยังเป็นของเก่าอยู่ 
# เช่น index ที่ 14 ถูกลบออกไปทำให้ index แสดงเป้น 13 -> 15 จำต้องทำการ reset_index
df.dropna(subset=['Product Name'])

# หลังจากใช้ func reset_index จะเห็นว่ามี col index เพิ่มขึ้นมา ซึ่งจะเป็น col index เราจำทำการลบทิ้งโดย เติม
# ใน function reset_index(drop=True) เพื่อให้ลบ col index เก่าออก
df.dropna(subset=['Product Name']).reset_index().head(20)

df = df.dropna(subset=['Product Name']).reset_index(drop=True)
df.head(20)

 ## เพิ่ม Col เพื่อจัด group ให้กับ product name

# iloc[row, col]
# Row ที่ 0 , แสดงทุก col
df.iloc[0, :]
# Row ที่ 1 , แสดงทุก col
df.iloc[1, :]

# show type
type(df.loc[0, 'Calories'])

np.isnan(df.loc[0, 'Calories']) # check numpy.float64 isnan

np.isnan(df.loc[1, 'Calories']) # check numpy.float64 isnan

# if col calories is null return product_name else null
df.apply(lambda r: r['Product Name'] if np.isnan(r['Calories']) else np.nan, axis=1)
df['categories'] = df.apply(lambda r: r['Product Name'] if np.isnan(r['Calories']) else np.nan, axis=1)
df.head()

# เติม row ที่เป็น null ด้านล่าง
df['categories'] = df['categories'].ffill()
df.head()

# drop row null
df = df.dropna(subset=['Calories']).reset_index(drop=True)
df.head(20)

# show desc
df.groupby('categories').describe()

# show column
df.columns

# reset sequence col name
df = df[['categories','Product Name', 'Label Wt (g)', 'Calories', 'Total fat (g)',
       'Saturated  Fat (g)', 'Trans Fat (g)', 'Cholesterol (mg)',
       'Sodium (mg)', 'Carbohydrates (g)', 'Fiber (g)', 'Sugar (g)',
       'Protein (g)', 'Vitamin A (%DV)', 'Vitamin C (%DV)', 'Calcium (%DV)',
       'Iron (%DV)']]
df.head()

# save to csv
df.to_csv('bakery_clean.csv', index=False)

# save to excel
df.to_excel('bakery_clean.xlsx', index=False)


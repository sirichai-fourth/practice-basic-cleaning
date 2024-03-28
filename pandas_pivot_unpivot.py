import pandas as pd

df=pd.read_csv('https://github.com/prasertcbs/tutorial/raw/master/wide.csv')
df

# Data pivot

df

# Data Unpivot

pd.melt(df, id_vars='branch')

df2 = pd.melt(df,id_vars='branch', var_name='menu', value_name='units')
df2

## การแสดงผลเพื่อจะวิเคราะห์ผลลัพธ์ แตกต่างกัน

## ข้อมูลที่ pivot สามารถ analytic ข้อมูลเบื้องต้นได้สะดวกกว่า

df.describe()

## ข้อมูลที่ unpivot จะสามารถ analytic ได้แค่ข้อมูลที่เป็น numeric

df2.describe()

## ข้อมูลที่ unpivot ก็สามารถดูข้อมูลได้ด้วย การ groupby

df2.groupby('menu').describe()

df2.groupby('branch').describe()

## สามารถ Transpose ให้ดูข้อมูลได้ง่ายขึ้น

df2.groupby('menu').describe().T

df2.groupby('branch').describe().T

# Corr หรือ Correlation ทำให้สามารถดูความสัมพันธ์ระหว่าง Col ได้
#   จากที่เห็นข้อมูลที่ = 1 จะหมายถึงว่า เป็นข้อมูลที่มีความสัมพันธ์กันที่สุด
#   ส่วนข้อมูลที่ cross กันแล้ว มีค่าเข้าใกล้ 1 ก็จะแสดงให้เห็นว่าข้อมูลนั้น อาจจะมีความสัมพันธ์กันตามค่าข้อมูล



df.corr()

# unpivot multi ids

df=pd.read_csv('https://github.com/prasertcbs/tutorial/raw/master/wide2.csv')
df

df2 = pd.melt(df, id_vars=['branch','period'], var_name='menu', value_name='unit')
df2

## จะเห็นว่ามอง col peroid เป็น numeric ทำให้ถูกนำมาคิดเวลาจะแสดง analytic เบื้องต้น

df2.describe()

## ต้องทำการ groupby เพื่อที่จะดูค่าของ period

df2.groupby('period').describe()

df2.groupby('period').describe().T


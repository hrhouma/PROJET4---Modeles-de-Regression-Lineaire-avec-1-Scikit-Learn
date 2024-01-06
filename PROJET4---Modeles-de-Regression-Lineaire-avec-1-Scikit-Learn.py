# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from sklearn import linear_model
from google.colab import files
uploaded = files.upload()

import io
data= pd.read_csv(io.BytesIO(uploaded['00 kc_house_data.csv']))
#print(data.head())
#print(data.tail())
#data.shape
#data.columns
dummyWaterfront=pd.get_dummies(data.waterfront)
dummyWaterfront.rename(columns = {0:'no_waterfront', 1:'yes_waterfront'}, inplace = True)
#print(dummyWaterfront)
dummyCondition=pd.get_dummies(data.condition)
dummyCondition.rename(columns = {1:'condition1', 2:'condition2',3:'condition3',4:'condition4',5:'condition5'}, inplace = True)
#print(dummyCondition)
merge=pd.concat([data,dummyWaterfront,dummyCondition],axis='columns')
#merge.head()
#merge.columns
finalData=merge.drop(['id','date','view', 'floors','waterfront','condition','grade','sqft_lot','bathrooms','sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode','lat', 'long', 'sqft_living15', 'sqft_lot15'],axis='columns')
finalData=finalData.drop(['no_waterfront'],axis='columns')
finalData.head()
finalData.head()
#x=finalData.drop(['price','condition1'],axis='columns')
x = finalData[['sqft_living','bedrooms','yes_waterfront','condition2', 'condition3', 'condition4', 'condition5']]
y=data['price']
print(x)

linreg=linear_model.LinearRegression()
linreg.fit(x,y)
print(linreg.intercept_)
print(linreg.coef_)

linreg.predict([[3000,4,0,0,0,1,0]])

sqft_living = 3000
bedrooms = 4
waterfront = 0
condition = 1
print("the price of a home with following characteristics: sqft_living= %f, bedrooms= %d, waterfront= %d, condition=%d is " % (sqft_living, bedrooms,waterfront,condition))
print(linreg.predict([[3000,4,0,0,0,0,0]]))

sqft_living = 3000
bedrooms = 4
waterfront = 0
condition = 2
print("the price of a home with following characteristics: sqft_living= %f, bedrooms= %d, waterfront= %d, condition=%d is " % (sqft_living, bedrooms,waterfront,condition))
print(linreg.predict([[3000,4,0,1,0,0,0]]))

sqft_living = 3000
bedrooms = 4
waterfront = 0
condition = 3
print("the price of a home with following characteristics: sqft_living= %f, bedrooms= %d, waterfront= %d, condition=%d is " % (sqft_living, bedrooms,waterfront,condition))
print(linreg.predict([[3000,4,0,0,1,0,0]]))

sqft_living = 3000
bedrooms = 4
waterfront = 0
condition = 4
print("the price of a home with following characteristics: sqft_living= %f, bedrooms= %d, waterfront= %d, condition=%d is " % (sqft_living, bedrooms,waterfront,condition))
print(linreg.predict([[3000,4,0,0,0,1,0]]))

sqft_living = 3000
bedrooms = 4
waterfront = 0
condition = 5
print("the price of a home with following characteristics: sqft_living= %f, bedrooms= %d, waterfront= %d, condition=%d is " % (sqft_living, bedrooms,waterfront,condition))
print(linreg.predict([[3000,4,0,0,0,0,1]]))
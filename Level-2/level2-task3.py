import pandas as pd 
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Dataset.csv')
data['Restaurant Name Length']= data['Restaurant Name'].apply(lambda x: len(x))
data['Address Length']= data['Address'].apply(lambda x:len(x))

label_encoder=LabelEncoder()
data['Has Table booking Encoded']= label_encoder.fit_transform(data['Has Table booking'])
data['Has Online delivery Encoded']= label_encoder.fit_transform(data['Has Online delivery'])

print(data.head())


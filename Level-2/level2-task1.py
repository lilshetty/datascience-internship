import pandas as pd

data=pd.read_csv('Dataset.csv')

data['Has Online delivery']=data['Has Online delivery'].map({'Yes':1,'No':0})
data['Has Table booking']=data['Has Table booking'].map({'Yes':1,'No':0})

table_booking_percent=(data['Has Table booking'].sum()/len(data))*100
online_delivery_percent=(data['Has Online delivery'].sum()/len(data))*100

print(f"Percentage of restaurants offering table booking: {table_booking_percent}%")
print(f"Percentage of restaurants offering online delivery: {online_delivery_percent}%")

avg_rating_with_booking=data[data['Has Table booking']==True]['Aggregate rating'].mean()
avg_rating_without_booking=data[data['Has Table booking']==False]['Aggregate rating'].mean()

print(f"Average rating with table booking {avg_rating_with_booking}")
print(f"Average rating without table booking {avg_rating_without_booking}")

price_ranges=data['Price range'].unique()

for price in price_ranges:
    subset=data[data['Price range']==price]
    online_delivery_percent=(subset['Has Online delivery'].sum()/len(subset))*100
    print(f"price range: {price}, Online delivery precentage: {online_delivery_percent}%")
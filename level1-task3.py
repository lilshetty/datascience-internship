#Level 1- Task 3
import folium
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Dataset.csv")

m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

for _, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(m)

m.save("restaurant_map.html")

city_distribution = data['City'].value_counts()
plt.figure(figsize=(12, 6))
city_distribution.plot(kind='bar')
plt.title('Restaurant Distribution by City')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.show()

correlation_latitude_rating = data['Latitude'].corr(data['Aggregate rating'])
correlation_longitude_rating = data['Longitude'].corr(data['Aggregate rating'])

print(f"Correlation between Latitude and Rating: {correlation_latitude_rating}")
print(f"Correlation between Longitude and Rating: {correlation_longitude_rating}")

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Dataset.csv')
most_common_pricerange= data['Price range'].mode()[0]
print(f"The most common price range is{most_common_pricerange}")

average_ratings= data.groupby('Price range')['Aggregate rating'].mean().reset_index()
print("average rating for each price range: ")
print(average_ratings)

max_rating= average_ratings['Aggregate rating'].max()
color_highest= average_ratings.loc[average_ratings['Aggregate rating']==max_rating,'Price range'].values[0]
print(f"The color representing the highest average rating is {color_highest}")

plt.figure(figsize=(8,6))
plt.bar(average_ratings['Price range'], average_ratings['Aggregate rating'], color='lightblue')
plt.xlabel('Price range')
plt.ylabel('Average rating')
plt.title('Average Ratings by Price Range')
plt.show()
# Level 1 : Task 2
import pandas as pd

data = pd.read_csv('Dataset.csv')

numerical_stats = data.describe()
print("Basic Statistical Measures for Numerical Columns:")
print(numerical_stats)

country_counts = data["Country Code"].value_counts()
print("\nDistribution of Country Code:")
print(country_counts)

city_counts = data["City"].value_counts()
print("\nDistribution of City:")
print(city_counts)

cuisine_counts = data["Cuisines"].value_counts()
print("\nDistribution of Cuisines:")
print(cuisine_counts)

top_cuisines = cuisine_counts.head(10)
print("\nTop 10 Cuisines with the Highest Number of Restaurants:")
print(top_cuisines)

top_cities = city_counts.head(10)
print("\nTop 10 Cities with the Highest Number of Restaurants:")
print(top_cities)
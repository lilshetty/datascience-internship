# Level 1 : Task 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset.csv')
num_rows, num_columns = df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)
plt.hist(df['Aggregate rating'], bins=20, edgecolor='k')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Aggregate Rating')
plt.show()
class_counts = df['Target_Column'].value_counts()
print("Class Counts:\n", class_counts)

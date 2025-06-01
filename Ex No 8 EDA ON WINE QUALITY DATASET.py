# Install Required Libraries
#pip install pandas seaborn matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df_red = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", delimiter=";")
df_white = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", delimiter=";")

# Display Information
print(df_red.info())
print(df_red.describe())

# Visualize Quality Count
sns.set(rc={'figure.figsize': (10, 6)})
sns.countplot(x='quality', data=df_red)
plt.title("Wine Quality Distribution")
plt.show()

# Visualize Alcohol Content Distribution
sns.histplot(df_red['alcohol'], bins=20, kde=True)
plt.title("Alcohol Content Distribution")
plt.show()

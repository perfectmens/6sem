import pandas as pd
import numpy as np
import seaborn as sns

# Load dataset
df = pd.read_csv('titanic.csv')

# View data
df.head()
df.info()
df.describe()

# Check duplicates
df.duplicated().sum()

# Unique values
df['Pclass'].unique()
df['Survived'].unique()
df['Sex'].unique()

# Plot unique values
sns.countplot(x='Pclass', data=df)

# Check and replace null values
df.isnull().sum()
df.replace(np.nan, '0', inplace=True)
df.isnull().sum()

# Filter data
df[df['Pclass'] == 1].head()

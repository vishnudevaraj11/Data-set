import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create the DataFrame
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Study Hours': [1, 2, 3, 4, 5, 6, 7],
    'Sleep Hours': [8, 7, 6, 2, 3, 4, 1],
    'Score': [45, 50, 55, 70, 60, 80, 85]
}

df = pd.DataFrame(data)

# Step 2: Display the data
print("Dataset:\n", df)

# Step 3: Correlation matrix (FIXED)
print("\nCorrelation Matrix:\n", df.corr())

# Step 4: Visualizations

# Scatter Plot: Study Hours vs Score
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Study Hours', y='Score', hue='Student')
plt.title('Study Hours vs Score')
plt.show()

# Scatter Plot: Sleep Hours vs Score
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Sleep Hours', y='Score', hue='Student')
plt.title('Sleep Hours vs Score')
plt.show()

# Pairplot (optional)
sns.pairplot(df[['Study Hours', 'Sleep Hours', 'Score']])
plt.suptitle('Pairwise Relationships', y=1.02)
plt.show()

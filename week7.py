# Data Analysis and Visualization Assignment
# Author: [Votre Nom]
# Dataset: Iris dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ---------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------

try:
    # Load Iris dataset from sklearn
    iris_sklearn = load_iris()
    df = pd.DataFrame(data=iris_sklearn.data, columns=iris_sklearn.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_sklearn.target, iris_sklearn.target_names)

    # Display first few rows
    print("First 5 rows of the dataset:")
    display(df.head())

    # Check data types and missing values
    print("\nDataset info:")
    print(df.info())
    print("\nMissing values per column:")
    print(df.isnull().sum())

except Exception as e:
    print(f"Error loading dataset: {e}")

# ---------------------------
# Task 2: Basic Data Analysis
# ---------------------------

try:
    # Basic statistics
    print("\nBasic statistics for numerical columns:")
    display(df.describe())

    # Grouping by species and computing mean
    print("\nAverage values per species:")
    display(df.groupby('species').mean())

    # Example observation
    print("\nObservation: Setosa tends to have smaller petal length and width compared to Versicolor and Virginica.")

except Exception as e:
    print(f"Error during analysis: {e}")

# ---------------------------
# Task 3: Data Visualization
# ---------------------------

# Set seaborn style for aesthetics
sns.set(style="whitegrid")

try:
    # 1. Line chart: simulate trends over index
    plt.figure(figsize=(8,5))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(subset.index, subset['sepal length (cm)'], label=species)
    plt.title("Sepal Length Trend by Species")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.show()

    # 2. Bar chart: average petal length per species
    plt.figure(figsize=(6,4))
    df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color='skyblue')
    plt.title("Average Petal Length per Species")
    plt.ylabel("Petal Length (cm)")
    plt.xlabel("Species")
    plt.show()

    # 3. Histogram: distribution of sepal width
    plt.figure(figsize=(6,4))
    plt.hist(df['sepal width (cm)'], bins=15, color='salmon', edgecolor='black')
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(6,4))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
    plt.title("Sepal Length vs Petal Length by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend()
    plt.show()

except Exception as e:
    print(f"Error during visualization: {e}")

# ---------------------------
# Findings / Observations
# ---------------------------

print("""
Findings:
1. Setosa has smaller petals and sepals compared to Versicolor and Virginica.
2. Petal length increases consistently from Setosa -> Versicolor -> Virginica.
3. Sepal width is fairly normally distributed across all species.
4. Scatter plots show a clear separation between Setosa and the other species, while Versicolor and Virginica overlap slightly.
""")

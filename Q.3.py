import pandas as pd
import numpy as np

df = pd.read_csv("filled_test.csv", header="infer")

# Statistical Measures:

num_cols = df.select_dtypes(include=['int64', 'float64'])
cat_cols = df.select_dtypes(include=['object'])

print("===== NUMERICAL COLUMNS =====")

for col in num_cols:
    print(f"\n--- {col} ---")
    print("Count:", df[col].count())
    print("Sum:", df[col].sum())
    print("Min:", df[col].min())
    print("Max:", df[col].max())
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Mode:", df[col].mode()[0])
    print("Range:", df[col].max() - df[col].min())
    print("Variance:", df[col].var())
    print("Standard Deviation:", df[col].std())

print("\n===== CATEGORICAL COLUMNS =====")

for col in cat_cols:
    print(f"\n--- {col} ---")
    print("Count:", df[col].count())
    print("Mode:", df[col].mode()[0])
    print("Unique Values:", df[col].nunique())
    print("Value Counts:\n", df[col].value_counts())

# Display all the unique value counts and unique values of all the columns of the dataset:

for col in df.columns:
    print(f"\n===== COLUMN: {col} =====")
    unique_vals = df[col].unique()
    print("Unique Values:\n", unique_vals)
    print("Number of Unique Values:", df[col].nunique())
    print("Value Counts:\n", df[col].value_counts())



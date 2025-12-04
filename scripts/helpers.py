# helpers.py
# Simple helper functions for Student Performance EDA

import seaborn as sns
import matplotlib.pyplot as plt

def show_missing(df):
    return df.isnull().sum()

def plot_count(df, col, title=""):
    plt.figure(figsize=(7,4))
    sns.countplot(data=df, x=col)
    plt.title(title or f"{col} Count")
    plt.xticks(rotation=45)
    plt.show()

def plot_dist(df, col, title=""):
    plt.figure(figsize=(7,4))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(title or f"{col} Distribution")
    plt.show()

def plot_box(df, x, y, title=""):
    plt.figure(figsize=(7,4))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title or f"{y} vs {x}")
    plt.xticks(rotation=45)
    plt.show()

def plot_heatmap(df, title="Correlation Heatmap"):
    plt.figure(figsize=(7,5))
    sns.heatmap(df.corr(), annot=True, cmap="viridis")
    plt.title(title)
    plt.show()

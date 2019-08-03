import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def get_boxplot(df, col):
    df.boxplot(column=col)

def get_violinplot(df, col):
    sns.violinplot(col, data=df)

def get_bar(df, col):
  df[col].value_counts().plot.bar()

def get_scatter(x, y, area, colors, opacity):
    plt.scatter(x, y, s=area, c=colors, alpha=opacity)
    plt.show()

def get_hist(df, col):
    df[col].hist()

def get_scatter_matrix(df):
    pd.plotting.scatter_matrix(df)
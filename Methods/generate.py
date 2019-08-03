import pandas as pd

def export_data(df, root):
  return df.to_csv(root)

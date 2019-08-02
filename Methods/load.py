import pandas as pd

def import_data(root):
  return pd.read_csv(root)

def get_data_frame(data):
  return pd.DataFrame(data)

def get_copy(df):
  return df.copy()

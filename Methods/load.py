import pandas as pd

def import_data(root, second_time=False):
  if second_time: 
    return pd.read_csv(root, index_col=0)
  return pd.read_csv(root)

def get_data_frame(data):
  return pd.DataFrame(data)

def get_copy(df):
  return df.copy()

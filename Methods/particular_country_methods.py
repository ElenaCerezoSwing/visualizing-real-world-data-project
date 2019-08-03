from cleaning import *
from conversions import *
import pandas

def get_country_data(df, country):
  country_df = df[df['country'] == country]
  country_df.drop(country_df[(country_df['UFO_shape'] == 'unknown') & 
      (country_df['length_of_encounter_seconds'] < 300)].index)

def get_au_data(df):
    return get_country_data(df, 'au')

def get_us_data(df):
    return get_country_data(df, 'us')

def get_ca_data(df):
    return get_country_data(df, 'ca')
    
def get_gb_data(df):
    return get_country_data(df, 'gb')


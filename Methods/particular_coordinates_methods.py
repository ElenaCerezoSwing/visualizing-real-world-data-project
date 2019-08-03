from cleaning import *
from conversions import *
import pandas

def get_cleaned_coordinates(df):
    df['latitude'] = remove_characters_in_strings(df, 'latitude', 'q')
    df['latitude'] = conver_item_to_number_type(df, 'latitude', float)
    df['latitude'] = get_truncate_values(df, 'latitude', 2)
    df['longitude'] = get_truncate_values(df, 'longitude', 2)
    df['points'] = list(zip(df['latitude'], df['longitude']))
    return df
    
from cleaning import *
from extractions import *
from conversions import *
import pandas

def get_cleaned_date_and_time(df): 
    df['Date'] = extract_by_index_and_separator(df, 'Date_time', ' ', 0)
    df['Date'] = clean_blank_spaces(df, 'Date')
    df['time'] = extract_by_index_and_separator(df, 'Date_time' , ' ', 1)
    df['months_aux'] = split_data_by_separator(df,'Date', '/')
    df['months']= extract_item_by_index(df, 'months_aux', 0 )
    df['years'] = extract_item_by_index(df, 'months_aux', 2 )
    df['years'] = conver_item_to_number_type(df, 'years', int)
    df['months'] = conver_item_to_number_type(df, 'months', int)
    df.drop(['described_duration_of_encounter', 'months_aux'], axis ='columns', inplace = True)
    df['length_of_encounter_seconds'] = conver_item_to_number_type(df, 'length_of_encounter_seconds', float)
    return df


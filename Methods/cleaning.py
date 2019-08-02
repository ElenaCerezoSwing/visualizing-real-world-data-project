
def drop_na_values(df, col):
    return df.drop(df[(df[col].isnull())].index)

def filter_dataframe_by_column_value(df, col, value):
    return df[df[col] == value]

def drop_na_values_in_more_cols(df, columns_to_clean):
    df2 = df.copy()
    for item in columns_to_clean:
        df2 = drop_na_values(df2, item) 
    return df2

def clean_blank_spaces(df,col):
    return df[col].str.strip()

def remove_characters_in_strings(df, col, rep):
    return [str(item).replace(rep, '') for item in df[col]]


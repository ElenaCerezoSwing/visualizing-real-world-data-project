
# The methods cointained in this files are supposed to be used just for clean data.
# It means, all of input should be non null or able to be converted into a specified type

def extract_by_index_and_separator(df, col, separator, index):
    return [item.split(separator)[index] for item in df[col]]

def split_data_by_separator(df, col, separator):
    return [item.split(separator) for item in df[col]]

def extract_item_by_index(df, col, index):
    return [item[index] for item in df[col]]

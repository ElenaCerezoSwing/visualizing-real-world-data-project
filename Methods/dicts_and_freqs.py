def get_frequencies(df, col):
    dictionary = {}
    sorted_df_col = sorted(df[col])
    unique_items = set(df[col])
    for item in unique_items:
        dictionary[item] = sorted_df_col.count(item)
    
    return dictionary


def get_frequencies_from_string_data(df, col):
    dictionary = {}
    my_list = list(df[col])
    unique_items = set(df[col])
    for item in unique_items:
        dictionary[item] = my_list.count(item)
    
    return dictionary

def get_list_indexes(our_list):
    return [our_list.index(item) for item in our_list]
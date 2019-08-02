
# The methods cointained in this files are supposed to be used just for clean data.
# It means, all of input should be non null or able to be converted into a specified type

# Returns items converted into integers
def apply_to_int(df, col):
    return [int(item) for item in df[col]]

# Returns items converted into floats
def apply_to_float(df, col):
    return [float(item) for item in df[col]]

# Returns items converted into specified type of number passed as a parameter
def conver_item_to_number_type(df, col, typ):
    return [typ(item) for item in df[col]]

# Returns truncated values fixed to n decimals passed as a parameter
def get_truncate_values(df, col, decimals):
    return [round(float(item),decimals) for item in df[col]]

# Return plain coordinates tupla
def get_tupla_plain_coordinates(df, lat, long):
    return list(zip(df[lat], df[long]))
import pandas as pd

def convert_numeric_cols(data):
    """Convert numeric columns to numeric types"""

    object_cols = ['Series', 'Series Code', 'Country Name', 'Country Code']
    all_cols = data.columns
    floating_cols = list(set(all_cols) - set(object_cols))

    for year in floating_cols:
        data[year] = pd.to_numeric(data[year], errors='coerce')

def extract_countries(data, storage_path, save=False):
    """Create a dataframe of each country's data"""

    countries_list = list(set(data['Country Name']))
    for country in countries_list:
        try:
            country_name = (country.replace(' ', '_') + '_data').lower()
            country_data = data[data['Country Name'] == country]
        except AttributeError:
            print(country, 'is not a country')

    if save:
        path = storage_path + country_name + '.csv'
        country_data.to_csv(path)
    else:
        return country_data

def define_df(country_name):
    country_name.lower()
    path = '../data/countries/' + country_name + '_data.csv'
    df = pd.read_csv(path)
    return df

def fix_year_cols(df):
    """Create easy-to-read columns for years"""
    col_list = df.columns
    fixed_cols = [year.split(' ')[0] for year in col_list]
    return fixed_cols

def transpose_helper(df):
    """Takes care of the logistics before the final transposition of a DataFrame"""
    unnecessary_cols = ['Series Code', 'Country Name', 'Country Code']
    df.drop(columns=unnecessary_cols, inplace=True, axis=1)
    df.columns = fix_year_cols(df)
    df.set_index('Series', inplace=True)
    return df.transpose()

    df.set_index('Series', inplace=True)
    return df.transpose()

def transpose_df(country_name):
    """Transposes and renames a dataframe"""
    df = define_df(country_name)
    transposed = transpose_helper(df)
    transposed.columns.name = country_name
    return transposed

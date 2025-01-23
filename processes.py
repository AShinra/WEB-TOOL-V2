import pandas as pd
import json


def clean_file(excel_file):
    # step 1 convert file to dataframe
    df = pd.read_excel(excel_file)

    # step 2 trim whitespaces from each column
    cols = df.columns
    for col in cols:
        try:
            df[col].str.strip()
        except:
            continue

    # step 3 remove duplicates
    df = df.drop_duplicates(keep='first')

    # step 4 remove publications included in blacklist
    f = open('json files/publications_remove.json')
    data = json.load(f)
    blacklist = data['remove']

    df = df[~df['Publication'].isin(blacklist)]

    return df



# remove rows based on publications to be ignored
def filter_rows_by_values(df, col, values):
    return 

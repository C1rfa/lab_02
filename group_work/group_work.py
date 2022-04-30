import pandas as pd


def get_sorted_birth_dates(asc = False):
    df = pd.read_csv('./group_work/group_list.csv')

    df['birth_date'] = pd.to_datetime(df['birth_date'], format="%d.%m.%Y")

    return df.sort_values(by="birth_date", ascending = asc)
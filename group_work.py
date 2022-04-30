import pandas as pd


group_list = pd.read_csv("./group_list.csv")

group_list['birth_date'] = pd.to_datetime(group_list["birth_date"], format=f"%d.%m.%Y")

print(group_list.sort_values(by="birth_date", axis=0, ascending=False))
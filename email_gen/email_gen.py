from os import sep
import random
import re

import pandas as pd


def generate_email_address ():

    #website name
    websites = pd.read_csv('./email_gen/website_classification.csv')
    rand_num = random.randint(0, len(websites['website_url']))
    website_name = re.findall(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]", websites['website_url'][rand_num])[0]

    if website_name[0] == 'w':
        website_name = website_name[4:]
    
    #username generation
    nicks = pd.read_csv('./email_gen/nicknames.csv')
    names = pd.read_csv('./email_gen/names.csv', sep=',' , on_bad_lines='skip').dropna()
    final_name = ''

    use_nick = bool(random.getrandbits(1))

    if use_nick:
        rand_num = random.randint(0, len(nicks['nicknames']))
        final_name = nicks['nicknames'][rand_num]
    else: 
        rand_first_num = random.randint(0, names.shape[0] - 1)
        rand_second_num = random.randint(0, names.shape[0] - 1)
        seps = ['_', '.']

        final_name = names[names.columns[0]][rand_first_num] + seps[random.randint(0, len(sep))] + names[names.columns[0]][rand_second_num]

    return final_name + "@" + website_name
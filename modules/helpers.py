from typing import final
from modules.constants import HOME_DIR
import os
from datetime import datetime

# Create a folder structure that looks like this /recon/domain/ and return the path to it


def make_directory(domain):
    today = datetime.today().strftime('%Y-%m-%d')
    folder = f'{HOME_DIR}/recon/{domain}/{today}/'
    os.makedirs(folder)
    return folder


# Loads a txt file and return a list of the strings contained in it
def load_txt(file):
    domains = []
    with open(file) as f:
        for d in f.readlines():
            domains.append(d.replace('\n', ''))
    return domains


# Remove elements that doesnt have the current domain name
def get_urls(domain, list_of_urls):
    final_list = [i for i in list_of_urls if domain in i]
    return final_list


# Loads different lists unify them and remove duplicates
def remove_duplicates_from_lists(*lists):

    final_result = set()

    for list_ in lists:
        for item in list_:
            final_result.add(item)
    
    return final_result


def save_to_file(set_of_subdomains):
    with open('alive-subdomains.txt', 'w') as file:
        for subdomain in set_of_subdomains:
            file.write(subdomain + '\n')
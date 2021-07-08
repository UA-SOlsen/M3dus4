from typing import final
from modules.constants import HOME_DIR
import os

# Create a folder structure that looks like this /recon/domain/ and return the path to it


def make_directory(domain):
    folder = '{home_dir}/recon/{target}'.format(
        home_dir=HOME_DIR, target=domain)
    os.makedirs(folder)
    return folder


# Loads a txt file and return a list of the strings contained in it
def load_txt(file):
    domains = []
    with open(file) as f:
        for d in f.readlines():
            domains.append(d.replace('\n', ''))
    return domains


def get_urls(domain, list_of_urls):
    final_list = []
    for i in list_of_urls:
        if domain in i:
            final_list.append(i)
    return final_list


# Loads different lists unify them and remove duplicates
def remove_duplicates_from_lists(*lists):
    final_result = set()

    for list_ in lists:
        for item in list_:
            final_result.add(item)
    
    return final_result
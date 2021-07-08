from os import remove
from modules.helpers import remove_duplicates_from_lists
from modules.input import validate_input
from subdomains import assetfinder, sublist3r
from misc import waybackurls, logo
from scanners import httprobe


def run():

    logo.load()
    domains = validate_input()

    for domain in domains:
        sublist3r_subs = sublist3r.run(domain)
        assetf_subs = assetfinder.run(domain)
        wayback_subs = waybackurls.run(domain)
        
        unified_domains = remove_duplicates_from_lists(sublist3r_subs, assetf_subs, wayback_subs)

    alive_subdomains = httprobe.run(unified_domains)
    print(alive_subdomains)


if __name__ == '__main__':
    run()

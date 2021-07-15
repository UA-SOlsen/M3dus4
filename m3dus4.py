from modules.helpers import remove_duplicates_from_lists, save_to_file, make_directory
import modules.input as input
from subdomains import assetfinder, sublist3r, omnisint
from misc import logo, waybackurls
from scanners import httprobe, aquatone
import logging

logging.basicConfig(filename='main.log', level=logging.DEBUG)


def run():

    logo.load()
    domains = input.validate_input()

    for domain in domains:
        directory = make_directory(domain)

        omnisint_subs = omnisint.run(domain)
        sublist3r_subs = sublist3r.run(domain)
        assetf_subs = assetfinder.run(domain)
        wayback_subs = waybackurls.run(domain)

        logging.debug(omnisint_subs, sublist3r_subs, assetf_subs, wayback_subs)
        unified_domains = remove_duplicates_from_lists(
            sublist3r_subs, assetf_subs, wayback_subs, omnisint_subs)

        live_subdomains = httprobe.run(unified_domains)
        live_subdomains_file = save_to_file(directory, live_subdomains)
        aquatone.run(live_subdomains_file, directory)


if __name__ == '__main__':
    run()

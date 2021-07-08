import argparse
from modules.helpers import load_txt


def parse_args():

    parser = argparse.ArgumentParser(description='Recon suite')
    parser.add_argument('-d', '--domain', help="Domain name to enumerate")
    parser.add_argument(
        '-l', '--list', help="Load a list of domains to enumerate")
    return parser.parse_args()


def validate_input():
    args = parse_args()
    domain = []
    if args.domain is not None:
        domain.append(args.domain)
        return domain
    else:
        return load_txt(args.list)

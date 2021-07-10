import subprocess
from modules.helpers import get_urls


def run(domain):
    process = subprocess.run(
        ['assetfinder', '--subs-only', '{}'.format(domain)], capture_output=True, text=True)
    output = process.stdout.split('\n')
    subdomains = get_urls(domain, output)
    return subdomains

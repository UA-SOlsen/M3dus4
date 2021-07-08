import subprocess
from modules.constants import HOME_DIR
from modules.helpers import get_urls

def run(domain):
    process = subprocess.run(['python3', '{}/tools/Sublist3r/sublist3r.py'.format(HOME_DIR),'-n', '-d', '{domain}'.format(domain=domain)], text=True, capture_output=True)
    output = process.stdout.split('\n')
    subdomains = get_urls(domain, output)
    subdomains.pop(0)
    return subdomains

 
        
            
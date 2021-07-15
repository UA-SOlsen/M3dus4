import requests


def run(domain):
    omnisint_query = 'https://sonar.omnisint.io/subdomains/{domain}'.format(
        domain=domain)
    try:
        response = requests.get(omnisint_query)
        return response.json()
    except requests.ConnectionError:
        return None
    

import requests
import json


def run(domain):
    crtsh_query = 'https://crt.sh/?q={domain}&output=json'.format(
        domain=domain)
    try:
        response = requests.get(crtsh_query)
        content = response.content.decode('UTF-8')
        json_data = json.loads(content)
        subdomains = set()
        wildcard_domains = set()
        for i in range(len(json_data)):
            name_value = str(json_data[i]['name_value'])
            if name_value.find('\n'):
                subdomains_list = name_value.split('\n')
                for subname_value in subdomains_list:
                    if subname_value.find('*'):
                        if subname_value not in subdomains:
                            subdomains.add(subname_value)
                    else:
                        if subname_value not in wildcard_domains:
                            wildcard_domains.add(subname_value)

        return subdomains
    except requests.ConnectionError:
        return False

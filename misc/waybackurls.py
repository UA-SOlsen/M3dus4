import requests
import json


BASE_URL = 'http://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&fl=original&collapse=urlkey'


def run(domain):
    def get_information(domain):

        r = requests.get(BASE_URL.format(domain))
        results = r.json()
        return results[1:]

    def get_subdomains(results):
        subdomains = set()

        # split('/')[2])

        for i in results:
            for j in i:
                subdomains.add(str(j).split('/')[2])
        return subdomains

    results = get_information(domain)
    subdomains = get_subdomains(results)
    return subdomains

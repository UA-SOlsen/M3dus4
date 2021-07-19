import requests
import threading
import queue
import time
from requests import sessions
from requests import exceptions
from requests.exceptions import ConnectTimeout
from urllib3.exceptions import NewConnectionError
import logging

logging.basicConfig(filename='httprobe.log', level=logging.DEBUG)


def run(subdomains):
    print('starting httprobe')
    start = time.time()

    alive_subdomains = set()

    def test_for_HTTP(subdomain):

        HTTP_url = 'http://'+subdomain
        try:
            resp = requests.get(HTTP_url, timeout=3, allow_redirects=False)

            if resp.status_code != 408:
                alive_subdomains.add(HTTP_url)

        except ConnectionRefusedError:
            pass
        except ConnectTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.InvalidURL:
            pass

    def test_for_HTTPS(subdomain):
        HTTPS_url = 'https://'+subdomain

        try:
            resp = requests.get(HTTPS_url, timeout=3, allow_redirects=False)

            if resp.status_code != 408:
                alive_subdomains.add(HTTPS_url)

        except ConnectionRefusedError:
            pass
        except ConnectTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.InvalidURL:
            pass

    for sub in subdomains:
        test_for_HTTP(sub)
        test_for_HTTPS(sub)

    end = time.time()
    return alive_subdomains

import subprocess

def run(alive_subdomains, folder_to_save):
    subprocess.run(f'cat {alive_subdomains} | aquatone -out {folder_to_save} -chrome-path /etc/chromium -silent', shell=True)
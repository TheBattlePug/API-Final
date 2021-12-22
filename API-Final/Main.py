import requests

def print_whole_website(link):
    r = requests.get(link)
    print(r.text + '\n')
    return

def print_headers(link):
    r = requests.get(link)
    print(r.headers + '\n')
    return+
import requests
import re

def print_whole_website(link):
    r = requests.get(link)    
    print(r.text + '\n')
    return


def print_headers(link):
    r = requests.get(link)
    print(r.headers['Content-Type'] + '\n')
    return


print_whole_website('http://www.sosmath.com/trig/Trig5/trig5/trig5.html')
 

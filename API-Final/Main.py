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

def get_image_links(link):
    r = requests.get(link)
    website_code = r.text

    image_links = []

    last_index = website_code.index("<p>")    
    while last_index < len(website_code):
        index_of_image_begin = website_code.find("<img", last_index) 
        index_of_image_end = website_code.find(">", index_of_image_begin) + 2

        if(index_of_image_end < len(website_code)):
            image_link = website_code[index_of_image_begin : website_code.find(">", index_of_image_begin)]
            image_links.append(image_link)
            print(image_link)

        last_index = index_of_image_end
    
    return

   

get_image_links('http://www.sosmath.com/trig/Trig5/trig5/trig5.html')
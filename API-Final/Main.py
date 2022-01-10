"""

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
    website_code = (r.text).lower()

    image_links = []

    last_index = 0  
    while last_index < len(website_code):
        index_of_image_begin = website_code.find("<img", last_index) 
        index_of_image_end = website_code.find(">", index_of_image_begin) + 1

        if(index_of_image_begin == -1):
            #print()
            find_link_from_code(image_links, link)
            return image_links    
         
        if(index_of_image_end < len(website_code)):
            image_link = website_code[index_of_image_begin : index_of_image_end]
            image_links.append(image_link)
            #print(image_link)

        last_index = index_of_image_end
        
    find_link_from_code(image_links, link)
    return image_links

def find_link_from_code(list_of_images, website_link):

    index = 0
    for link in list_of_images:
        beggining = link.find("src=\"") + 5
        end = link.find("\"", beggining)
        link = link[beggining : end]
        raw_link = website_link[0: website_link.find(".html")]
        list_of_images[index] = raw_link + "/" + link
        #print(list_of_images[index])
        index += 1
    
    return   

# get_image_links('http://www.sosmath.com/trig/Trig5/trig5/trig5.html')
# print("end")

"""
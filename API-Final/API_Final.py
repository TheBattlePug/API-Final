import requests

"""
#here is the part where you can request an article and its elements
r = requests.get('https://xkcd.com/1906/')

print(r.status_code)

print(r.headers)

print('\n' + r.headers['Content-Type'])

print('\n' + r.text)

#image
recieve = requests.get('https://imgs.xkcd.com/comics/mkaing_progress.png')

with open(r'C:\Inputs\DansCat.jpg','wb') as f:
    f.write(recieve.content)

print("\n It works ... finally")
"""

#passing argument in the request

ploads = {'things':2, 'total': 25}
r = requests.get('https://httpbin.org/get', params=ploads)
print(r.text)

#Using POST Request

pload = {'username': 'Olivia', 'password': '123'}
r = requests.post('https://httpbin.org/post', data = pload)

r_dictionary = r.json()

print('')

print(r_dictionary['form'])

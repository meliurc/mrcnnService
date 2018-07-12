# -*- coding: utf-8 -*-

import requests

# url = "http://ec2-18-210-230-107.compute-1.amazonaws.com/countme/waht"
# r = requests.get(url=url)
# print r.content

#

url = "http://ec2-18-210-230-107.compute-1.amazonaws.com/pic"

file_name = './panda.jpg'
newname = file_name.split('/')
print newname[len(newname)-1]

files = {'file': (newname, open(file_name, 'rb'), 'image/jpg')}
r = requests.post(url, files=files)
result = r.text

print result
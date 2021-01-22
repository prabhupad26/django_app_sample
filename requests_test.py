import requests

r_get = requests.get('https://www.python.org')
print(r_get.text)
print("*"*50)
print("*"*50)
print("*"*50)



payload = dict(key1='value1', key2='value2')
r_post = requests.post('https://httpbin.org/post', data=payload)
print (r_post.text)
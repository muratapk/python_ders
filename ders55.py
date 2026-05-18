import requests
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
veri=response.json()
print(veri)
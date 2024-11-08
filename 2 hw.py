import requests as req

url = 'https://jsonplaceholder.typicode.com/posts'
par = {
    'userId' : 1
}

res = req.get(url,params=par)
print(res.text)
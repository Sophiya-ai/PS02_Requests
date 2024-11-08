import requests as req

url = 'https://jsonplaceholder.typicode.com/posts'
data_new = {
    'title' : 'foo',
    'body' : 'bar',
    'userId' : '1'
}

res = req.post(url,data=data_new)
print(res.status_code)
print(f'ANSWER - {res.json()}')
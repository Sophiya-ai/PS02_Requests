import requests as rec
import pprint

# response = rec.get('https://api.github.com/')
# # print(response.status_code)
# # if response.ok:
# #     print('Request is succesfull')
# # else:
# #     print('error')
# print(response.text)
# res_json = response.json()
# pprint.pprint(res_json)
#print(response.content)

# params = {
#     'q' : 'JavaScript' #q-query
# }
# response = rec.get('https://api.github.com/search/repositories', params=params)
# res_json = response.json()
# #pprint.pprint(res_json)
# print(f'Количество репозиториев с использованием JS - {res_json['total_count']}')

# img = 'https://yastatic.net/naydex/yandex-search/Q14CE4C04/a6b330-fWGfG/IDM_jNAamz460oF8xMVirtSsSHtcrzQH_9RAwK1MxfWJpZZASm_VFyiaiEJs29QxAFQJd22F_jU_FRrcXeoWBkVC2bnDz898mAGhbOWFFt-ULQho_tnG9Y1iQ5JueodUiJUmMV86NKZKKC'
# response = rec.get(img)
# with open ("test.jpg",'wb') as file:
#     file.write(response.content)

# response = rec.get('https://google.com/')
# print(response.status_code)
# print(response.headers) #заголовки
# print(response.text)

url = 'https://jsonplaceholder.typicode.com/posts' #бесплатный онлайн сервис для тестирования
data = {
    'title' : 'test post request',
    'body' : 'test content of the post request',
    'userID' : 2
}

response = rec.post(url,data=data)
print(response.status_code)
print(f'answer - {response.json()}')
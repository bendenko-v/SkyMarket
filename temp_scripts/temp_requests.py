import requests

url = 'http://127.0.0.1:8000/api/ads/'

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Njk4NTc1LCJpYXQiOjE2ODU2OTQ5NzUsImp0aSI6ImZlZGQzZWQ1MTU3YjRmZTViNDU4MjI3YzBlNjFhZmVjIiwidXNlcl9pZCI6MzR9.Sf5jB6HIRHWx6DAYjtKZDEOrkCujVHFV-5IhAyadTB8'
}

data = {
    'title': 'Фигурка симпсона',
    'price': 11000,
    'description': 'Крутая фигурка! Берите пока есть)',
}

with open('bart.jpg', 'rb') as image_file:
    image = image_file.read()

image_data = {
    'image': ('bart.jpg', image)
}
# POST query
response = requests.post(url, headers=headers, data=data, files=image_data)

print(response.content.decode('utf-8'))

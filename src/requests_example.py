import requests

with requests.get('https://jsonplaceholder.typicode.com/todos/1') as response:
    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    pass
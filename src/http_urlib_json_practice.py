import json
from urllib import request


a = list([1,2,3,4])

with request.urlopen('https://jsonplaceholder.typicode.com/todos/1') as f:
    text = f.read()
    todo = json.loads(text, encoding='utf-8')

    user = {
        'userName': 'POS'
    }

    print(todo['userId'])
    print(user.userName)

if __name__ == '__main__':
    pass
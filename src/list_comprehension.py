
def return_a_list():
    return [n+1 for n in range(0, 11) if n < 8]


if __name__ == '__main__':
    print(return_a_list())

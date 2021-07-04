from string import Template
import re


def main():
    print(Template(" value 1: ${x} : value 2: ${y}").substitute({'x': ' x axis', 'y': 'y axis'}))
    print(re.sub('fuck', 'f*ck', 'fuck this fucking bullshit'))


if __name__ == '__main__':
    main()


from enum import Enum


class FileType(Enum):
    IMAGE = 'image',
    VIDEO = 'video',
    TEXT_FILE = 'text'


def main():
    file_type = 'text'.strip()

    if file_type == FileType.IMAGE.value:
        print('An image!')
    elif file_type == FileType.TEXT_FILE.value:
        print('A text file!')


if __name__ == '__main__':
    main()

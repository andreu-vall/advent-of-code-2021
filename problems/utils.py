import os
import requests


def get_lines(day):
    if not os.path.exists(path := get_path(day)):
        download_file(day)

    with open(path, 'r') as f:
        return [line.rstrip() for line in f]


def get_path(day):
    return f'input/input{str(day).zfill(2)}.txt'


def download_file(day):
    url = f'https://adventofcode.com/2021/day/{day}/input'
    request = requests.get(url, cookies=get_cookies())
    with open(get_path(day), 'wb') as f:
        f.write(request.content)


def get_cookies():
    with open('../session_cookie.txt', 'r') as f:
        return {'session': f.read()}

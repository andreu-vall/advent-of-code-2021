import os
import requests


def get_input(day):
    if not os.path.exists(path := get_path(day)):
        download_file(day)

    with open(path, 'r') as f:
        return [line.rstrip() for line in f]


def get_path(day):
    return f'input/input{day}.txt'


def download_file(day):
    url = f'https://adventofcode.com/2021/day/{day}/input'
    request = requests.get(url, cookies=get_cookies())
    with open(get_path(day), 'wb') as f:
        f.write(request.content)


def get_cookies():
    with open('session_cookie.txt', 'r') as f:
        return {'session': f.read()}


def int_lines(day):
    return list(map(int, get_input(day)))


def split_lines(day):
    lines = [line.split() for line in get_input(day)]
    for line in lines:
        for i in range(len(line)):
            if line[i].isdecimal():
                line[i] = int(line[i])
    return lines

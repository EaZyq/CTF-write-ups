#!/usr/bin/python3
# -*- coding:utf-8 -*-

data = open('./trainfuck.tf', 'r').read()
mapping = {
    '🚅': '>',
    '🚄': '<',
    '🚆': '[',
    '🚃': '-',
    '🚇': ']',
    '🚂': '+',
    '🚈': '.',
    '🚉': ','
}

c = {}

for char in data:
    if char not in c:
        c[char] = 1
    else:
        c[char] += 1

for i in c:
    print(i, c[i])

for k in mapping:
    data = data.replace(k, mapping[k])

with open('./out.bf', 'w+') as f :
    f.write(data)

#!/usr/bin/python3
import sys
import argparse
import os

def ellipsize(text, maxlen=1):
    assert maxlen > 0

    if len(text) <= maxlen:
        return text
    else:
        return "{}…".format(text[:maxlen - 1])

def pathtrunc(pathtext, pathlimit):
    if pathtext.startswith('/'):
        leadingslash = '/'
        pathtext = pathtext[1:]
    else:
        leadingslash = ''

    path = pathtext.split('/')
    limit = pathlimit - len(path)

    plens = list(map(len, path))

    if limit < len(path):
        return leadingslash + "/".join(map(ellipsize, path))
    else:
        while sum(plens) > limit:
            print(repr(plens))
            maxpl = 0
            print('mpl = {maxpl}'.format(**locals()))
            while maxpl < len(plens) and plens[maxpl] <= 1:
                maxpl += 1
            print('mpl = {maxpl}'.format(**locals()))
            if maxpl == len(plens):
                break
            print('mpl = {maxpl}'.format(**locals()))
            for i, secl in enumerate(plens):
                if secl - i > plens[maxpl] - maxpl and secl > 1:
                    maxpl = i
            print('mpl = {maxpl}'.format(**locals()))

            if plens[maxpl] > 1:
                plens[maxpl] -= 1
            else:
                break

        for i, (sec, plen) in enumerate(zip(path, plens)):
            path[i] = ellipsize(sec, maxlen=plen)

        return leadingslash + '/'.join(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('len', type=int)

    args = parser.parse_args()

    path = args.path
    home = os.getenv('HOME')
    if home:
        if home.endswith('/'):
            home = home[:-1]

        if path.startswith(home):
            path = '~{}'.format(path[len(home):])

    print(pathtrunc(path, args.len))

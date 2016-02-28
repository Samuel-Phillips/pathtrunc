#!/usr/bin/python3
import sys
import argparse
import os
import ctypes

try:
    _wcswidth = ctypes.CDLL('libc.so.6').wcswidth
    _wcswidth.argtypes = [ctypes.c_wchar_p, ctypes.c_size_t]
    _wcswidth.restype = ctypes.c_int

    def wcswidth(s):
        return _wcswidth(s, len(s))
except:
    wcswidth = len


def ellipsize(text, maxlen=1):
    assert maxlen > 0

    if wcswidth(text) <= maxlen:
        return text
    else:
        n = 1
        while wcswidth(text[:-n]) > maxlen - 1:
            n += 1
        return "{}…".format(text[:-n])

def pathtrunc(pathtext, pathlimit):
    if pathtext.startswith('/'):
        leadingslash = '/'
        pathtext = pathtext[1:]
    else:
        leadingslash = ''

    if pathtext.endswith('/'):
        pathtext = pathtext[:-1]

    path = pathtext.split('/')
    limit = pathlimit - len(path)

    plens = list(map(wcswidth, path))

    if limit < len(path):
        return leadingslash + "/".join(map(ellipsize, path))
    else:
        while sum(plens) > limit:
            maxpl = 0
            while maxpl < len(plens) and plens[maxpl] <= 1:
                maxpl += 1
            if maxpl == len(plens):
                break
            for i, secl in enumerate(plens):
                if secl - i > plens[maxpl] - maxpl and secl > 1:
                    maxpl = i

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

#!/usr/bin/python3
import sys

path = sys.argv[1].split('/')
LIMIT = int(sys.argv[2]) - len(path)
plens = [len(sec) for sec in path]
if LIMIT < len(path):
    print("/".join(("…" if len(sec) > 0 else "") for sec in path))
else:
    while sum(plens) > LIMIT:
        maxpl = 0
        for i, secl in enumerate(plens):
            if secl - i > plens[maxpl] - maxpl:
                maxpl = i

        if plens[maxpl] > 0:
            plens[maxpl] -= 1
        else:
            for i, secl in enumerate(plens):
                if secl > 0:
                    plens[i] -= 1
                    break
            else:
                print("/".join(("…" if len(sec) > 0 else "") for sec in path))
                exit(0)

    for i, (sec, plen) in enumerate(zip(path, plens)):
        if plen < len(sec):
            path[i] = sec[:plen - 1] + '…'

    print('/'.join(path))


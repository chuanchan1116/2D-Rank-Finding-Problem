#!/usr/bin/env python3

global rank

class Point:
    def __init__(self, i, p):
        self.i = i
        self.x, self.y = p

def findRank(p):
    if len(p) <= 1:
        return p
    i, li, ri = 0, 0, 0
    l = findRank(p[:int(len(p)/2)])
    r = findRank(p[int(len(p)/2):])
    while True:
        if l[li].y <= r[ri].y:
            p[i] = l[li]
            li += 1
            if li >= len(l):
                for _ in r[ri:]:
                    rank[_.i] += li
                    p[i+1] = _
                    i += 1
                break
        else:
            p[i] = r[ri]
            rank[r[ri].i] += li
            ri += 1
            if ri >= len(r):
                p[i+1:] = l[li:]
                break
        i += 1
    return p

while True:
    n = int(input())
    if n == 0:
        break
    point = []
    rank = [0] * n
    for i in range(n):
        point.append(Point(i, [int(_) for _ in input().strip().split()]))
    point.sort(key=lambda p: (p.x, p.y))
    findRank(point)
    print(' '.join(map(str, rank)))

#https://www.hackerrank.com/challenges/circular-array-rotation/problem
#!/bin/python3

import sys

def circularArrayRotation(a, m, k):
    start = len(a) - k % len(a)
    rotated = []
    for i in range(start, len(a)):
        rotated.append(a[i])
    for i in range(0, start):
        rotated.append(a[i])
    result = []
    for i in m:
        result.append(rotated[i])
    return result

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, m, k)
    print ("\n".join(map(str, result)))



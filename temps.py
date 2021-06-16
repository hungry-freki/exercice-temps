import sys

def time(h, m, s):
    h = 60
    m = 60
    s = 60
    while s > 59 or m > 59:
        if s > 59:
            S = s // 60
            s = s % 60
            m = S + m
        if m > 59:
            M = m // 60
            m = m % 60
            h = M + h
    return (h, m, s)
#__name__=="__main__"

print(time)
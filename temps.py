import sys

def time(h, m, s):

    while s > 59 or m > 59:
        if s > 59:
            sec = s // 60
            s = s % 60
            m = sec + m
        if m > 59:
            min = m // 60
            m = m % 60
            h = min + h
    return (h, m, s)
__name__=="__main__"

print(time[1, 60, 60])

#blabla
#aaaaaa
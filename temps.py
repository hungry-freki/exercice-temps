
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
    print(h, "heures,", m, "minutes, ", s, "secondes")

time(400-71, 40+6, 10*5)
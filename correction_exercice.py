import sys

def convertisseur(h, m, s):
	while s > 59 or m > 59:
		if s > 59:
		    S = s // 60
		    s = s % 60
		    m = S + m
		if m > 59:
		    M = m // 60
		    m = m % 60
		    h = M + h
	
	return((h,m,s))

if __name__ == '__main__':
	solution = convertisseur(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
	print(solution)




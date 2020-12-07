def solve(l, i, j, right, down):
	tot = 0
	rightmostBound = len(l[0])
	bottomBound = len(l)
	#go right 3, down 1, until rightmost bound, then use modulo from there, until bottomBound is hit
	start = l[i][j]
	while i <> bottomBound-1:
		j = (j+right)%rightmostBound
		i += down
		if l[i][j]=='#':
			tot+=1
		print i,j, l[i][j]
	return tot
	

with open("input.txt") as f:
	l = map(lambda s: s.strip('\n'), f.readlines())
	print solve(l, 0, 0,1,1)*solve(l, 0, 0,3,1)*solve(l, 0, 0,5,1)*solve(l, 0, 0,7,1)*solve(l, 0, 0,1,2)

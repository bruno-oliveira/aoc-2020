import math;

def solve(s):
	#F lower, B upper
	#L lower, R upper
	lowerrow = 0.0
	row = 127.0
	lowerseat = 0.0
	seat = 7.0
	for c in s:
		print (lowerrow+row)/2.0
		if c=='F':
			row = math.floor((lowerrow+row)/2.0)
		if c=='B':
			lowerrow = math.ceil((lowerrow+row)/2.0)
		if c=='L':
			seat = math.floor((seat+lowerseat)/2.0)
		if c=='R':
			lowerseat = math.ceil((seat+lowerseat)/2.0)
	return int(lowerrow*8+lowerseat)

with open("input.txt") as f:
	l = map(str.strip, f.readlines())
	#max(map(solve, l))
	s = sorted(map(solve, l))
	for i in range(1, len(s)):
		if s[i]-s[i-1]>1:
			print "ans "+str(s[i]-1)
		

def solve(l):
	first = 0
	last = len(l)-1
	while first < last:
		if l[first]+l[last]==2020:
			print l[first]*l[last]
			break
		elif l[first]+l[last]<2020:
			first+=1
		else:
			last-=1
			
def solve2(l,i):
	first = 0
	last = len(l)-1
	while first < last:
		if first==i:
			first+=1
		if last==i:
			last-=1
		if l[first]+l[last]==2020-l[i]:
			print l[first]*l[last]*l[i]
			break
		elif l[first]+l[last]+l[i]<2020:
			first+=1
		else:
			last-=1

with open("input.txt") as f:
	l = sorted(map(lambda n: int(n) ,f.readlines()))
	for i in range(len(l)):
		solve2(l,i)

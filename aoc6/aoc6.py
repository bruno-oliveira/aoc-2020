def solve(l):
    supportSet = set()
    for elem in l:
        for i in range(0,len(elem)):
            supportSet.add(elem[i:i+1])
    return sum(map(lambda s: len(s), supportSet))

#Bag of words approach, set-ify everything and check per number of groups, add to
#running total
def solve2(l):
    bag = set()
    for elem in l:
        for i in range(0,len(elem)):
            bag.add(elem[i:i+1])
    maxGroups = len(l)
    cnt = 0
    ans = 0
    for c in bag:
        for elem in l:
            if c in elem:
                cnt+=1
        if cnt==maxGroups:
            ans+=1
        cnt=0
    return ans
    
    
with open("input.txt") as f:
    l=map(str.strip, f.readlines())

    grouped = []
    inner = []
    for s in l:
        if s <> '':
            inner.append(s)
        else:
            grouped.append(inner)
            inner = []
    grouped.append(inner)
    print sum(map(solve2, grouped))

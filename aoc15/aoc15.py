from array import array

input_puzzle = [0,12,6,13,20,1,17]
sample0 = [3,1]

def solve(n, lines):
        if n <= len(lines):
            return int(lines[n - 1])
        last = lines[-1]
        seen = array('I', (0, ) * (max(n - 1, *lines) + 1))
        for i, x in enumerate(lines[:-1]):
            seen[x] = i + 1
        for i in range(len(lines), n):
            next = i - (seen[last] or i)
            seen[last] = i
            last = next
        return last

freq = {}
last_idx = {}

for e in sample0:
    freq[e]=1
for i in range(len(sample0)):
    last_idx[sample0[i]]=[i,i]


latest = len(sample0)
while latest <= 2020:
    print "latest: ",latest
    if freq.get(sample0[len(sample0)-1])==1:
        sample0.append(0)
        freq[0]=freq.get(0,0)+1
        if sample0[len(sample0)-1] in last_idx.keys():
            snd = last_idx[sample0[len(sample0)-1]][1]
            last_idx[sample0[len(sample0)-1]] = [snd, len(sample0)-1]
        else:
            last_idx[sample0[len(sample0)-1]] = [len(sample0)-1, len(sample0)-1]
    else:
        if freq.get(sample0[len(sample0)-1])>=2:
           newval = last_idx[sample0[len(sample0)-1]][1]-last_idx[sample0[len(sample0)-1]][0]
           sample0.append(newval)
           if newval in freq.keys():
               last_idx[sample0[len(sample0)-1]] = [last_idx[sample0[len(sample0)-1]][1], len(sample0)-1]
               freq[sample0[len(sample0)-1]]+=1
           else:
               last_idx[sample0[len(sample0)-1]] = [len(sample0)-1,len(sample0)-1]
               freq[sample0[len(sample0)-1]]=1
    latest = latest+1

freqs = {}
for i in sample0:
    if i in freqs.keys():
        freqs[i]+=1
    else:
        freqs[i]=1
        
for j in range(len(sample0)):
    if sample0[j]==0:
        print j
    
print solve(30000000, [0,12,6,13,20,1,17])

'''
3, 1, 2, 0, 0, 1, 4, 0, 3, 8, 0, 3, 3
3, 1, 0, 0, 1, 3, 5, 0, 4, 0, 2, 0, 2, 2, 1, 10,
3, 0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0,
2, 0, 0, 1, 0, 2, 5, 0, 3, 0, 2, 5,
1, 0, 0, 1, 2, 0, 3, 0, 2, 4, 0, 3

0 377
1 80
2 30
3 57
4 140
5 121
6 109
7 60
8 30
9 31
'''

'''
f(4) = 0 if freq(f(3))=1
       or last[f(3)]-prevtolast[f(3)] if freq(f(3)) > 1

f(n) = 0 if freq(f(n-1))=1
       or lastseen[f(n-1)]-prevtolastseen[f(n-1)] if freq(f(n-1)) > 1

f(0)=3  freq(f(0))=1
f(1)=1  freq(f(1))=1
f(2)=2  freq(f(2))=1

f(3)= 0  freq(f(3))=1
f(4)= 0  freq(f(4))=2
f(5)= lastseen[f(4)]-prevtolastseen[f(4)] = 4-3=1 freq(f(5))=2
f(6)= lastseen[f(5)]-prevtolastseen[f(5)] = 5-1=4 freq(f(6))=1
'''

    
    

#Sample input uses preamble 5
def canMatchSumInPreamble(list_slice, target):
    sums = {}
    for elem in list_slice:
        sums[elem] = 0
        sums[target-elem] = 0
    for elem in list_slice:
        sums[elem] += 1
        if target - elem >= 0:
            sums[target-elem] +=1
    tot = 0
    for e in sums:
        if sums[e]==2 and (e in list_slice):
            tot += 1
            if tot==2:
                return True
                break
    return False

def preprocessSums(l):
    accumulated = []
    accumulated.append(l[0])
    for i in range(1, len(l)):
        accumulated.append(l[i]+accumulated[i-1])
    #print accumulated
    return accumulated

with open("input.txt") as f:
    l=map(lambda s: int(s), map(str.strip, f.readlines()))
    preamble = 25
    target = 0
    for i in range(0, len(l)-preamble):
        if not canMatchSumInPreamble(l[i:i+preamble],l[preamble+i]):
            target=l[preamble+i]
            break
    #[1,2,3,4,5,6,7] --> (2,4)=12
    #[1,3,6,10,15,21,28] ---> aux[4]-aux[1]=12    
    aux = preprocessSums(l)
    for i in range(0, len(aux)):
        for j in range(i+1, len(aux)):
            if aux[j]-aux[i]==22406676:
                print i,j
                print max(l[i+1:j])+min(l[i+1:j])
                break
    

import copy;

def getFirstSeat(l, i, j, direction):
    current = l[i][j]
    maxL = len(l[0])-2
    maxB = len(l)-2
    if direction =='t':
        while i>0:
            i-=1
            if i >= 0:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='b':
        while i<=maxB:
            i+=1
            if i <= maxB+1:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='l':
        while j>0:
            j-=1
            if j >= 0:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='r':
        while j<=maxL:
            j+=1
            if j <= maxL+1:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='tl':
        while (i>0 and j>0):
            j-=1
            i-=1
            if j>=0 and i>=0:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='tr':
        while (i>0 and j<=maxL):
            j+=1
            i-=1
            if j<=maxL+1 and i>=0:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='bl':
        while (i<=maxB and j>0):
            j-=1
            i+=1
            print i,j
            if j>=0 and i<=maxB+1:
                current = l[i][j]
                if current <> '.':
                    return current
    if direction =='br':
        while (i<=maxB and j<=maxL):
            j+=1
            i+=1
            if j<=maxL+1 and i<=maxB+1:
                current = l[i][j]
                if current <> '.':
                    return current    

def will_change(l, i, j):
    top = getFirstSeat(l,i,j,'t')
    bottom = getFirstSeat(l,i,j,'b')
    left = getFirstSeat(l,i,j,'l')
    right = getFirstSeat(l,i,j,'r')
    topleft = getFirstSeat(l,i,j,'tl')
    topright = getFirstSeat(l,i,j,'tr')
    bottomleft = getFirstSeat(l,i,j,'bl')
    bottomright = getFirstSeat(l,i,j,'br')
    #neighb = [(i-1,j-1),(i-1,j),(i, j-1),(i,j+1),(i+1,j),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    neighb = [top, bottom, left, right,topleft, topright, bottomleft, bottomright]
    print neighb
    #valid = filter(lambda x: x[0]>=0 and x[0]<=len(l)-1 and x[1]>=0 and x[1]<=len(l[0])-1,neighb)
   # check = map(lambda t: l[t[0]][t[1]],valid)
    if l[i][j] == "L" and ("#" not in neighb):
        return True
    elif l[i][j] == "#" and neighb.count('#')>=5:
        return True
    elif l[i][j] == ".":
        return False
    else:
        return False
        

def solve(l):
    lprev = copy.deepcopy(l)
    for i in range(len(l)):
        for j in range(len(l[i])):
            #print "Will change for i="+str(i)+" j="+str(j)+" ,"+lprev[i][j]+ "==> "+str(will_change(lprev, i,j))
            if lprev[i][j] != "." and will_change(lprev, i,j):
                if lprev[i][j] == "L":
                    aux = list(l[i])
                    aux[j]='#'
                    #l[i] = ''.join(aux)
                elif lprev[i][j] == "#":
                    aux = list(l[i])
                    aux[j]='L'
                l[i] = ''.join(aux)
    if l==lprev:
        return l
    else:
        print l
        return solve(l)
                
with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    final = solve(l)
    print final
    print sum(map(lambda s: s.count('#'),final))

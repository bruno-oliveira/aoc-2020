def solve(l, colors, ans):
    tmp = l
    fstlevel=[]
    print "Colors are: ",colors
    for c in set(colors):
        print "color to filter:a",len(c)
        for x in tmp:
            if c in x.split("contain")[1]:
                fstlevel.append(x)
    print "fstlevel ",set(fstlevel)
    if fstlevel==[]:
        return ans
    colorsRecurse = []
    for e in fstlevel:
        colorsRecurse.append(e.split("contain")[0].strip())
    for clr in set(colorsRecurse):
        ans.append(clr)
    return solve(l,set(colorsRecurse), ans)


def allContainedBagsAreInBase(contained, base):
    aux = []
    for color in base:
        for v in contained:
            if color in v:
                aux.append(color)
    return len(aux)==len(contained)
                
def preprocessBaseValues(l):
    supportMap = {}
    noEmptyBags = filter(lambda x:"no other" not in x,l)
    for bags in noEmptyBags:
        supportMap[bags.split("contain")[0].strip()] = bags.split("contain")[1].strip()    
    colorsMap = {}
    base = map(lambda x:x.split("contain")[0].strip(), filter(lambda x:"no other" in x,l))
    for c in base:
        colorsMap[c] = 0
    for b in noEmptyBags:
        contained = map(str.strip, supportMap[b.split("contain")[0].strip()].split(","))
        if allContainedBagsAreInBase(contained,base):
                colorsMap[b.split("contain")[0].strip()] = sum(map(lambda qty: int(qty[0]), map(lambda s: s.split(" "), contained)))
    return colorsMap
    
    

#part 2 we need different processing, bottom-up - memoization
def solve(colorsMap, l, bag):
    start = filter(lambda v: v.startswith(bag), l)
    seeds = start[0].split("contain")[1].strip().split(", ")
    preprocess = map(lambda s: s.split(" "), seeds)
    vals = []
    for elem in preprocess:
        inn = []
        inn.append(int(elem[0]))
        inn.append(elem[1]+" "+elem[2])
        vals.append(inn)
        
    tot = []
    for quantityForColor in vals:
        if colorsMap.get(quantityForColor[1],"null") is "null":
            colorsMap[quantityForColor[1]] = solve(colorsMap, l, quantityForColor[1])
            soma = quantityForColor[0]*colorsMap[quantityForColor[1]]+quantityForColor[0]
            tot.append(soma)
        else:
            soma = quantityForColor[0]*colorsMap[quantityForColor[1]]+quantityForColor[0]
            tot.append(soma)
    return sum(tot)
        
                
with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    l=map(lambda s: str.replace(s,"bags",""),l)
    l=map(lambda s: str.replace(s,"bag",""),l)
    l=map(str.strip,l)
    colorsMap = preprocessBaseValues(l)
    print solve(colorsMap, l, 'shiny gold')

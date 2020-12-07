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

#part 2 we need different processing, bottom-up
def solve2(l, colors, ans):
    base = map(lambda x:x.split("contain")[0].strip(), filter(lambda x:"no other" in x,l))
    x=map(lambda x:x.split("contain")[1].strip(), l)
    for elem in x:
        z=map(str.strip , elem.split(","))
        for ii in z:
            if ii in base:
                


with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    l=map(lambda s: str.replace(s,"bags",""),l)
    l=map(lambda s: str.replace(s,"bag",""),l)
    l=map(str.strip,l)
    print solve2(l, ['shiny gold'], [])    

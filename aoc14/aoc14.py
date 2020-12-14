import copy;

def applyMaskToValue(mask, v):
    masked=""
    for i in range(len(mask)):
        if mask[i]=="X":
            masked+=v[i]
        else:
            masked+=mask[i]
    return int(masked, 2)

def applyMaskToMemoryLocation_part2(mask, idx, mapa, val, v):
    print "original memory location ",idx
    masked=""
    for i in range(len(mask)):
        if mask[i]=="X":
            masked+="X"
        elif mask[i]=="1":
            masked+="1"
        else:
            masked+=v[i]
            
    maskedAsList = list(masked)
    total = masked.count('X')
    for i in range(0,2**total):
        k = -1
        copied = copy.deepcopy(maskedAsList)
        for j in range(0, len(copied)):
            if copied[j]=='X':
                k+=1
                copied[j] = ('0'*(total-len(bin(i)[2:]))+bin(i)[2:])[k]
        print "Writing to address ",copied, int(''.join(copied), 2)
        mapa[int(''.join(copied), 2)]=value  
    print masked, total
    
with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    maskAndAddresses = map(lambda ins: ins.split(" = ")[0], l)
    values = map(lambda ins: ins.split(" = ")[1], l)
    mapa = {}
    mask = ""
    for i in range(len(l)):
        if "mask" in maskAndAddresses[i]:
            mask = values[i]
        else:
            fst = maskAndAddresses[i].split("[")
            idx = int(fst[1].split("]")[0])
            value = int(values[i])
            print applyMaskToMemoryLocation_part2(mask, idx, mapa, value,'0'*(36-len(bin(idx)[2:]))+bin(idx)[2:])
            
            #mapa[idx] = applyMaskToValue(mask, '0'*(36-len(bin(value)[2:]))+bin(value)[2:])
    print sum(mapa.values())
    
            
#'0'*(36-len(bin(11)[2:]))+bin(11)[2:]

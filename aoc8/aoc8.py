from copy import *

def parseInstruction(inst):
    singleInst = inst.split(" ")
    instType = singleInst[0]
    arg = singleInst[1]
    if instType == "nop":
        return None
    if instType == "acc":
        if arg[0]=='-':
            return ['a',-1*int(arg[1:])]
        else:
            return ['a',int(arg)]
    if instType == "jmp":
        if arg[0]=='-':
            return ['j',-1*int(arg[1:])]
        else:
            return ['j',int(arg)]

def runCode(instructionWithIdx):
    accumulator = 0
    hasBeenSeen = {}
    for elem in instructionWithIdx:
        hasBeenSeen[elem] = 0

    startInstruction = 0
    validToRun = True
    while validToRun:
        if startInstruction==len(hasBeenSeen)-1:
            return "acc is ",accumulator
            break;
        inst = instructionWithIdx[startInstruction]
        inst = inst.split(" ")[1]+" "+inst.split(" ")[2]
        p = parseInstruction(inst)
        hasBeenSeen[instructionWithIdx[startInstruction]] = hasBeenSeen[instructionWithIdx[startInstruction]]+1
        if hasBeenSeen[instructionWithIdx[startInstruction]]==2:
            return -1
        if p is None:
            startInstruction+=1
        elif p[0]=='j':
            startInstruction+=p[1]
        elif p[0]=='a':
            accumulator+=p[1]
            startInstruction+=1

            
with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    instructionWithIdx = [str(elem)+" "+l[elem] for elem in range(len(l))]
    allJmp = filter(lambda x: "jmp" in x, instructionWithIdx)
    allNop = filter(lambda x: "nop" in x, instructionWithIdx)

    allPossibleAns = []
    for elem in allJmp:
        instructionWithIdxCopy = deepcopy(instructionWithIdx)
        elem = elem.replace("jmp","nop")
        instructionWithIdxCopy[int(elem.split(" ")[0])]=elem
        allPossibleAns.append(runCode(instructionWithIdxCopy))
    for elem in allNop:
        instructionWithIdxCopy = deepcopy(instructionWithIdx)
        elem = elem.replace("nop","jmp")
        instructionWithIdxCopy[int(elem.split(" ")[0])]=elem
        allPossibleAns.append(runCode(instructionWithIdxCopy))

    print filter(lambda x: x<>-1,allPossibleAns)
    

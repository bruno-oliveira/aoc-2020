def evaluate(expr):
    expr = expr.replace(' ', '')
    left = ""
    operatorsSeen = 0
    currentSymbol = -1
    print "the expr",expr
    if expr.count("*")==1 and expr.count("+")==0:
        print "in"
        args = expr.split("*")
        args = map(int, args)
        print args
        return args[0]*args[1]
    if expr.count("+")==1 and expr.count("*")==0:
        args = expr.split("+")
        args = map(int, args)
        return args[0]+args[1]
    while operatorsSeen<2:
        currentSymbol+=1
        if expr[currentSymbol] == "+" or expr[currentSymbol]=="*":
            operatorsSeen+=1
        if operatorsSeen==2:
            break
        left += expr[currentSymbol]
    if "*" in left:
        args = left.split("*")
        args = map(int, args)
        print args[0]*args[1]
        return evaluate(str(args[0]*args[1])+expr[currentSymbol:])
    elif "+" in left:
        args = left.split("+")
        args = map(int, args)
        return evaluate(str(args[0]+args[1])+expr[currentSymbol:])        

def evaluateWithPrecedence(expr):
    onlySums = [n for n,x in enumerate(expr) if x=='+']
    onlyMults = [n for n,x in enumerate(expr) if x=='*']
    if len(onlySums)==0 or len(onlyMults)==0:
        return evaluate(expr)
    else:
        #Parse expr for args of +
        expr = expr.replace(' ', '')
        ops = [n for n,x in enumerate(expr) if x=='+' or x=='*']
        print ops
        for i in range(len(ops)):
            if expr[ops[i]]=='+':
                if i < len(ops)-1 and i <> 0:
                    return evaluateWithPrecedence(expr[0:ops[i-1]+1]+str(int(expr[ops[i-1]+1:ops[i]])+int(expr[ops[i]+1:ops[i+1]]))+expr[ops[i+1]:])
                elif i > 0:
                    return evaluateWithPrecedence(expr[0:ops[i-1]+1]+str(int(expr[ops[i-1]+1:ops[i]])+ int(expr[ops[i]+1:])))
                else:
                    return evaluateWithPrecedence(str(int(expr[0:ops[i]])+int(expr[ops[i]+1:ops[i+1]]))+expr[ops[i+1]:])
        
        
    
    
def getLastParenthesisExpression(expr):
    idxLastOpeningParen = -1
    endmatch = -1
    for i in range(len(expr)):
            if expr[i] == "(":
                idxLastOpeningParen = i
    if idxLastOpeningParen >= 0:
        for k in range(idxLastOpeningParen,len(expr)):
            if expr[k] == ")":
                endmatch = k
                break
            
    return (idxLastOpeningParen+1,endmatch)
        
    
def solve(expr):
    print expr
    j = 0
    if ("(" in expr) or (")" in expr):
        a,b=getLastParenthesisExpression(expr)
        return solve(expr[0:a-1]+str(evaluateWithPrecedence(expr[a:b]))+expr[b+1:])
    else:
        return evaluateWithPrecedence(expr)
    j+=1
            
            
print solve("6 + 9 * 8 + 6")
print solve("9 * 8 + 6")
print solve("6 + 9 * 8")
print solve("6 + (9 * 8) + 6")
print solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
print solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
print solve("6 + 9 * 8 + 6")
print solve("6 + 9 * 8 + 6")

ans=0
with open("input.txt") as f:
    l = map(str.strip, f.readlines())
    for e in l:
        ans+=solve(e)
print ans

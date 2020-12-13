def processStdDirections(typeInst, value, current, facing):
    if typeInst == 'N':
        upd= current[1]+value
        current = (current[0],upd)
        
    if typeInst == 'S':
        upd= current[1]-value
        current = (current[0],upd)
        
    if typeInst == 'E':
        upd= current[0]+value
        current = (upd,current[1])
        
    if typeInst == 'W':
        upd= current[0]-value
        current = (upd,current[1])
    return current

def processNavigationInstruction(current, facing, inst):
    value = int(inst[1:])
    typeInst = inst[0]
    current = processStdDirections(typeInst, value, current, facing)
    if typeInst == 'F':
        current = processStdDirections(facing, value, current, facing)
    if typeInst == 'L' and facing=='E':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'N'
        elif value == 2:
            facing = 'W'
        elif value == 3:
            facing = 'S'
        else:
            facing = 'E'
    if typeInst == 'L' and facing=='W':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'S'
        elif value == 2:
            facing = 'E'
        elif value == 3:
            facing = 'N'
        else:
            facing = 'W'
    if typeInst == 'L' and facing=='N':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'W'
        elif value == 2:
            facing = 'S'
        elif value == 3:
            facing = 'E'
        else:
            facing = 'N'
    if typeInst == 'L' and facing=='S':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'E'
        elif value == 2:
            facing = 'N'
        elif value == 3:
            facing = 'W'
        else:
            facing = 'S'
    if typeInst == 'R' and facing=='E':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'S'
        elif value == 2:
            facing = 'W'
        elif value == 3:
            facing = 'N'
        else:
            facing = 'E'
    if typeInst == 'R' and facing=='W':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'N'
        elif value == 2:
            facing = 'E'
        elif value == 3:
            facing = 'S'
        else:
            facing = 'W'
    if typeInst == 'R' and facing=='N':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'E'
        elif value == 2:
            facing = 'S'
        elif value == 3:
            facing = 'W'
        else:
            facing = 'N'
    if typeInst == 'R' and facing=='S':
        value = value/90
        value = value % 4
        if value == 1:
            facing = 'W'
        elif value == 2:
            facing = 'N'
        elif value == 3:
            facing = 'E'
        else:
            facing = 'S'
    return current,facing

def solve2(l):
    final = (0,0)
    waypoint = (10,1)
    current = (0, 0)
    for inst in l:
        value = int(inst[1:])
        typeInst = inst[0]
        if typeInst=='F':
            current = (current[0]+value*waypoint[0],current[1]+value*waypoint[1])
            final = (final[0]+current[0],final[1]+current[1])
        if typeInst=='N':
            waypoint = (waypoint[0],value+waypoint[1])
        if typeInst=='S':
            waypoint = (waypoint[0],waypoint[1]-value)
        if typeInst=='E':
            waypoint = (waypoint[0]+value,waypoint[1])
        if typeInst=='W':
            waypoint = (waypoint[0]-value,waypoint[1])
        if typeInst=='R':
            value = value/90
            value = value % 4
            if value == 1:
                waypoint = (waypoint[1], -1*waypoint[0])
            elif value == 2:
                waypoint = (-1*waypoint[0], -1*waypoint[1])
            elif value == 3:
                waypoint = (-1*waypoint[1],waypoint[0])
        if typeInst=='L':
            value = value/90
            value = value % 4
            if value == 1:
                waypoint = (-1*waypoint[1],waypoint[0])
            elif value == 2:
                waypoint = (-1*waypoint[0], -1*waypoint[1])
            elif value == 3:
                waypoint = ( waypoint[1],-1*waypoint[0])
        print current,waypoint


with open("input.txt") as f:
    l=map(str.strip, f.readlines())
    solve2(l)
##    facing = 'E'
##    current = (0,0)
##    for instruction in l:
##        a,b=processNavigationInstruction(current, facing, instruction)
##        print "facing ",facing
##        facing = b
##        current = a
##    print current

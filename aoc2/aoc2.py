def isValid(s):
	tot = 0
	trimmed = s.split(':')
	dbConstraints = trimmed[0].split(' ')
	bounds = map(lambda s: int(s), dbConstraints[0].split('-'))
	password = trimmed[1].strip(' ')
	for char in password:
		if char==dbConstraints[1]:
			tot+=1
	return tot>=bounds[0] and tot<=bounds[1]

def isValid2(s):
	tot = 0
	trimmed = s.split(':')
	dbConstraints = trimmed[0].split(' ')
	bounds = map(lambda s: int(s), dbConstraints[0].split('-'))
	password = trimmed[1].strip(' ')
	if (password[bounds[0]-1]==dbConstraints[1] or password[bounds[1]-1]==dbConstraints[1]) and password[bounds[0]-1] <> password[bounds[1]-1]:
		return True
	else:
		return False

with open("input.txt") as f:
	l = map( isValid2, map(lambda s: s.strip('\n'), f.readlines()))
	print len(filter(lambda e: e==True, l))

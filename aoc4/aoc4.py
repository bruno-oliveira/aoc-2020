with open("input.txt") as f:
	l = f.readlines()
	filtered = []
	singlePassport = ""
	for passport in l:
		if passport<>'\n':
			singlePassport+=passport.replace('\n',' ')	
		else:
			singlePassport=singlePassport.strip()
			filtered.append(singlePassport)
			singlePassport=""


def is_hex(s):
    hex_digits = set("0123456789abcdef")
    for char in s:
        if not (char in hex_digits):
            return False
    return True


def isValueValid(string, prop):
	value = string[string.find(prop)+4:].split(' ')[0]
	if prop=='byr':
		return len(value)==4 and (int(value)>=1920 and int(value)<=2002)
	if prop=='iyr':
		return len(value)==4 and (int(value)>=2010 and int(value)<=2020)
	if prop=='eyr':
		return len(value)==4 and (int(value)>=2020 and int(value)<=2030)
	if prop=='hgt':
		return len(value[:-2])>0 and ((int(value[:-2])>=150 and int(value[:-2])<=193 and value.endswith('cm'))  or (int(value[:-2])>=59 and int(value[:-2])<=76 and value.endswith('in')))
	if prop=='hcl':
		return value.startswith('#') and len(value[1:])==6 and is_hex(value[1:])
	if prop=='ecl':
		return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if prop=='pid':
		return len(value)==9
	
	
validFirst= filter(lambda passport: (('byr:' in passport) and ('iyr:' in passport) 
	and ('eyr:' in passport) and ('hgt:' in passport) and ('hcl:' in passport) and ('ecl:' in passport) and ('pid:' in passport)), filtered)
	
ans=0
for v in validFirst:
	if isValueValid(v,'byr') and isValueValid(v,'iyr') and isValueValid(v,'eyr') and isValueValid(v,'hgt') and isValueValid(v,'hcl') and isValueValid(v,'ecl') and isValueValid(v,'pid'):
		ans+=1
print ans+1 

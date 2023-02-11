def is_reflexive(A, R):
	for a in A:
		if not R(a,a):
			return False
	return True

def is_transitive(A, R):
	for x in A:
		for y in A:
			for z in A:
				if R(x,y) and R(y,z) and not R(x,z):
					return False
	return True

def notAntiReflexive_and_notReflexive(A, R):
	if not len(A):
		return True
	isRe = True
	isAntiRe = True
	for a in A:
		if isRe and not R(a, a):
			isRe = False
		elif isAntiRe and R(a, a):
			isAntiRe = False
		if not isRe and not isAntiRe:
			return True
	return False 
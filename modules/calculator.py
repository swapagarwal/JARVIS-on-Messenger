import math

def add(a, b):
	return a + b
	
def sub(a, b):
	return a - b
	
def mult(a, b):
	return a * b
	
def div(a, b):
	return a / b
	
def sin(a):
	return math.sin(a)
	
def cos(a):
	return math.cos(a)
	
def tan(a):
	return math.tan(a)
	
def asin(a):
	return math.asin(a)
	
def acos(a):
	return math.acos(a)
	
def atan(a):
	return math.atan(a)
	
def pow(a, b):
	return math.pow(a, b)
	
def log(x, base):
	return math.log(x, base)
	
def sqrt(x):
	return math.sqrt(x)
	
def addPolynom(coefs_a, coefs_b):
	tmp = zip(coefs_a, coefs_b)
	return t[0] + t[1] for t in tmp
	
def subPolynom(coefs_a, coefs_b):
	tmp = zip(coefs_a, coefs_b)
	return t[0] - t[1] for t in tmp


def derivePolynom(coefs):
	if(len(coefs) < 1):
		return coefs
	
	tmp = coefs[1:]
	for x in range(len(tmp)):
		tmp[x] = (x + 1) * tmp[x]
		
	return tmp

def integratePolynom(coefs):
	for x in range(len(coefs)):
		coefs[x] = coefs[x] / (x + 1)
	
	return 0 + coefs

def compute(parameters):
	

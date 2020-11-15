
def horner(poly,n,x):
	result = poly[0]
	for i in range(1,n):
		result=result*x+poly[i]
	return result

poly = [2,-6,2,-2]
x=3
n=len(poly)
print("giá trị đa thức: ",horner(poly,n,x))

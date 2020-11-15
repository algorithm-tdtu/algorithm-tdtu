
def compute_lcm(num1,num2):
	
	if num1>num2:
		greater=num1
	else:
		greater=num2
	while(True):
		if((greater%num1==0) and (greater%num2==0)):
			lcm=greater
			break
		greater+=1
	
	return lcm
num1=54
num2=24
print("not using gcd: ",compute_lcm(num1,num2))

#Using GCD
def compute_gcd(num1,num2):
	while(num2):
		num1,num2=num2,num1%num2
	return num1
def compute_lcm1(num1,num2):
	lcm=(num1*num2)//compute_gcd(num1,num2)
	return lcm
print("using gcd: ",compute_lcm1(num1,num2))
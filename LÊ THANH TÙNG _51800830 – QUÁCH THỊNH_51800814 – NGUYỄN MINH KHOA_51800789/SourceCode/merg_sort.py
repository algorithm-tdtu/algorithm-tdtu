import random
import time
start = time.time()
A = [random.randint(0,1000) for i in range(10000)]
B = [i for i in A]

def MergeSort(a,i,j):
	random.randint(i,j)
	
	if i==j:
		return a
	k=int((i+j-1)/2)
	MergeSort(a,i,k)

	MergeSort(a,k+1,j)
	Merge(a,i,k,j)

def Merge(a,i,k,j):
	p1=i
	p2=k+1
	p3=i
	B=[0]*len(a)
	while p1<=k and p2<=j:
		if a[p1]<=a[p2]:
			B[p3]=a[p1]
			p1+=1
		else:
			B[p3]=a[p2]
			p2+=1
		p3+=1
	while p1<=k:
		B[p3]=a[p1]
		p1+=1
		p3+=1
	while p2<=j:
		B[p3]=a[p2]
		p2+=1
		p3+=1
	for r in range(i,j+1):
		a[r]=B[r]

MergeSort(A,0,len(A)-1)
print("thời gian: ",time.time()-start)

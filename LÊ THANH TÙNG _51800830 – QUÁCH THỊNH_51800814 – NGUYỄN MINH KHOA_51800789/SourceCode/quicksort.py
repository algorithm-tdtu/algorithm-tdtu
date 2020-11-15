import random
import time


A = [random.randint(0,1000) for i in range(10000)]
B = [i for i in A]

def RandomQuicksort(A,i,j):
	random.randint(i,j)
	start = time.time()
	Quicksort(A,0,len(A)-1)
	print("Thời gian: ",time.time()-start)
	B.sort()

def Quicksort(a,i,j):
	if i<j:
		p=Partition(a,i,j)
		Quicksort(a,i,p-1)
		Quicksort(a,p+1,j)

def Partition(a,i,j):
	pivot=a[i]
	h=i
	for k in range(i+1,j+1):
		if a[k]<pivot:
			h+=1
			a[k],a[h]=a[h],a[k]
	a[h],a[i]=a[i],a[h]
	return h

RandomQuicksort(A,0,len(A)-1)

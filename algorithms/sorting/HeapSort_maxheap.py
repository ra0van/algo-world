# your code goes here
import math as m

def max_heapify(a,i):
	#print "heapify for ",i
	left = 2*i
	right = 2*i+1
	largest = i
	
	
	if left<len(a):
		if a[largest]<a[left]:
			largest = left
	if right <len(a):
		if a[largest]<a[right]:
			largest = right
	if largest!=i:
		a[i],a[largest] = a[largest],a[i]
		max_heapify(a,largest)

def Build_max_heap(a):
	n = int(m.floor(len(a)/2))
	for i in xrange(n-1,-1,-1):
		max_heapify(a,i)

a = [14,10,2,3,5,11,17,8,9]
Build_max_heap(a)
result = []
for i in xrange(len(a)-1,0,-1):
	root = a[0]
	result.append(root)
	a[i],a[0] = a[0],a[i]
	a.remove(root)
	#print "new heaP",a
	max_heapify(a,0)
result.append(a[0])
print result[::-1]
	

"""
	merge_sort.py
	Implementation of mergesort on a list and return a list
"""

def Merge(a,p,q,r):
	n = r-p+1
	s = [-1]*n
	i=j=k=0
	j = q
	print s
	while i<q+1 and j<n:
		if (a[i]<a[j]):
			s[k] = a[i]
			i += 1
		else:
			# print k,j
			s[k] = a[j]
			j += 1
		k += 1
	print i,j,k
	print q+1,n
	while i<q+1 and k<n:
		s[k] = a[i]
		k+=1
		i+=1

	while j<n and k<n:
		s[k] = a[j]
		k+=1
		j+=1
	print s
	return s

def MergeSort(a,p,r):
	q = (p+r)/2
	# print p,q,r
	if p<q:
		MergeSort(a,p,q)
		MergeSort(a,q+1,r)
		Merge(a,p,q,r)
	# else:
		# print p,q

def sort(seq):
	return MergeSort(seq,0,len(seq)-1)

print sort([3,2,1])
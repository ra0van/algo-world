"""
	insertion_sort.py

	Implementation of insertion sort on a list and return a sorted list.

"""

def sort(seq):
	for i in range(1,len(seq)):
		j = i-1
		key = seq[i]
		while seq[j]>key and j>=0:
			seq[j+1] = seq[j]
			j -= 1
		seq[j+1] = key
	return seq
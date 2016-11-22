# using divide and conquer method

import sys


def max_cross_subarray(a,low,mid,high):
	left_sum = -2147483647
	sum = 0
	max_left = -1
	for i in range(mid,low+1,-1):
		sum += a[i]
		if sum>left_sum:
			left_sum=sum
			max_left = i
	right_sum = -2147483647
	sum = 0
	max_right = -1
	for i in range(mid+1,high+1):
		sum += a[i]
		if sum>right_sum:
			right_sum = sum
			max_right = i
	return max_left,max_right,left_sum + right_sum

def max_subarray(a,low,high):
	if low==high:
		return low,high,a[low]
	else:
		mid = int((low+high)/2)
		left_low,left_high,left_sum = max_subarray(a,low,mid)
		right_low,right_high,right_sum = max_subarray(a,mid+1,high)
		cross_low,cross_high,cross_sum = max_cross_subarray(a,low,mid,high)
		
		if left_sum>=right_sum and left_sum>=cross_sum:
			return left_low,left_high,left_sum
		elif right_sum>=left_sum and right_sum>=cross_sum:
			return right_low,right_high,right_sum
		else:
			return cross_low,cross_high,cross_sum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]

left,right,sum = max_subarray(arr,0,len(arr)-1)
for i in range(left,right+1):
	print arr[i],
print "\n"+str(sum)

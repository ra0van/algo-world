import sys

def get_input():
	a = [-1,2,4,0]
	return a

# returns the power equal to or greater than
def get_nearest_power(num,base):
	p = 0
	n = 1
	while n<num:
		n = pow(base,p)
		p += 1
	return p

def construct_seg_tree(ip,seg_tree,low,high,root):
	if low==high:
		seg_tree[root] = ip[low]
		return
	mid = (low+high)/2
	left = 2*root + 1
	right = 2*root + 2
	construct_seg_tree(ip,seg_tree,low,mid,left)
	construct_seg_tree(ip,seg_tree,mid+1,high,right)
	seg_tree[root] = min(seg_tree[left],seg_tree[right])

def range_min_query(seg_tree,qlow,qhigh,low,high,root):
	if qlow<=low and qhigh>=high: #total overlap
		return seg_tree[root]

	if qlow>high or qhigh<low: #partial overlap
		return sys.maxint

	mid = (low+high)/2
	left = 2*root + 1
	right = 2*root + 2
	return min(range_min_query(seg_tree,qlow,qhigh,low,mid,left), range_min_query(seg_tree,qlow,qhigh,mid+1,high,right))


def main():
	ip = get_input()
	l = len(ip)
	p = get_nearest_power(l,2)
	seg_len = 2*(pow(2,p))-1
	seg_tree = [sys.maxint] * seg_len
	construct_seg_tree(ip,seg_tree,0,l-1,0)
	print seg_tree
	qlow = 0
	qhigh = 3
	print range_min_query(seg_tree,qlow,qhigh,0,l-1,0)
if __name__ == '__main__':
	main()
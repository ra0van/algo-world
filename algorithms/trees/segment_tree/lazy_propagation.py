import sys

def getInput():
	a = [-1,2,4,0]
	return a

# returns the power equal to or greater than
def getNearestPower(num,base):
	p = 0
	n = 1
	while n<num:
		n = pow(base,p)
		p += 1
	return p

def constructSegTree(ip,seg_tree,low,high,root):
	if low==high:
		seg_tree[root] = ip[low]
		return
	mid = (low+high)/2
	left = 2*root + 1
	right = 2*root + 2
	constructSegTree(ip,seg_tree,low,mid,left)
	constructSegTree(ip,seg_tree,mid+1,high,right)
	seg_tree[root] = min(seg_tree[left],seg_tree[right])

def rangeMinQuery(seg_tree,lazy,qlow,qhigh,low,high,root):

	if low>high:
		return sys.maxint

	if lazy[root]!=0:
		seg_tree[pos] += lazy[root]
		if low!= high:
			lazy[2*root+1 ] += lazy[root]
			lazy[2*root+2] += lazy[root]
		lazy[root] = 0

	if qlow<=low and qhigh>=high: #total overlap
		return seg_tree[root]

	if qlow>high or qhigh<low: #partial overlap
		return sys.maxint

	mid = (low+high)/2
	left = 2*root + 1
	right = 2*root + 2
	return min(rangeMinQuery(seg_tree,lazy,qlow,qhigh,low,mid,left), rangeMinQuery(seg_tree,lazy,qlow,qhigh,mid+1,high,right))


def updateSegTreeLazy(seg_tree,lazy,startRange,endRange,delta,low,high,pos ):
	if low>high:
		return

	if lazy[pos]!=0:
		seg_tree[pos] += lazy[pos]
		if low != high:
			lazy[2*pos + 1] += lazy[pos]
			lazy[2*pos + 2] += lazy[pos]
		lazy[pos] = 0

	#no overlap condition
	if startRange > high or endRange< low:
		return

	#total overlap condition
	if startRange<=low and endRange>=high:
		seg_tree[pos] += delta
		if low != high:
			lazy[2*pos + 1] += delta
			lazy[2*pos + 2] += delta
		return

	#partial overlap
	mid = (low+high)/2

	updateSegTreeLazy(seg_tree,lazy,startRange,endRange,delta,low,mid,2*pos+1)
	updateSegTreeLazy(seg_tree,lazy,startRange,endRange,delta,mid+1,high,2*pos+2)
	seg_tree[pos] = min(seg_tree[2*pos+1],seg_tree[2*pos+2])

def main():
	ip = getInput()
	l = len(ip)
	p = getNearestPower(l,2)
	seg_len = 2*(pow(2,p))-1
	seg_tree = [sys.maxint] * seg_len
	lazy = [0] * seg_len
	constructSegTree(ip,seg_tree,0,l-1,0)
	print seg_tree
	qlow = 0
	qhigh = 3
	print rangeMinQuery(seg_tree,lazy,qlow,qhigh,0,l-1,0)
	updateSegTreeLazy(seg_tree,lazy,0,3,2,0,l-1,0)
	print rangeMinQuery(seg_tree,lazy,qlow,qhigh,0,l-1,0)
if __name__ == '__main__':
	main()
import math

q = int(input())

for t in range(q):
	n = int(input())
	a = [int(i) for i in input().split()]
	cnt = {}
	for x in a:
		if not x in cnt:
			cnt[x] = 1
		else:
			cnt[x]+=1
	cnts = []
	for x in cnt.values():
		cnts.append(x)
	cnts.sort()
	cnts.reverse()
	curmin = cnts[0]
	res = 0
	for x in cnts:
		res += min(curmin, x)
		curmin = max(0, min(x-1, curmin-1))
	print(res)

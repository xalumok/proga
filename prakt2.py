a = list(map(float, input().split()))
isSorted = True
for i in range(len(a)-1):
	if a[i]>a[i+1]:
		isSorted = False

if isSorted:
	res = 1
	for i in range(len(a)-1):
		res *= a[i+1] - a[i]
	print(res)
else:
	res = 0
	for i in range(len(a)):
		if a[i]>0:
			res += a[i]
	print(res)

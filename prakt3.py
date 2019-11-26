def swapCols(a, x, y, n):
	for i in range(n):
		a[i][x], a[i][y] = a[i][y], a[i][x]

n, m, k  = map(int, input("input n, m, k: ").split())

k-=1

if n <= 0 or m <= 0:
	print("bad n or m value")
	exit(0)

if k >= n and k>=0:
	print("wrong K value")
	exit(0)

a = []
for i in range(n):
	row = list(map(int, input().split()))
	if (len(row) != m):
		print("bad matrix")
		exit(0)
	a.append(row)

for i in range(m):
	for j in range(i+1, m):
		if a[k][i]>a[k][j]:
			swapCols(a, i, j, n)

print()

for i in range(n):
	for j in range(m):
		print(a[i][j], end=" ")
	print()



#  ~~~ DOCUMENTATION ~~~

# Error messages:
# 	error - wrong K value
# 	Error - bad matrix
#	eRROR - bad n or m value

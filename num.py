import math

def Entropia(a):
	res = 0
	for x in a:
		if (x==0):
			continue
		res += -x * math.log(x, 2)
	return res

def Nadl(H, k):
	return 1 - H/math.log(k, 2)

def rowSum(a, ind):
	res = 0
	for i in range(3):
		res += a[ind][i]
	return res

def colSum(a, ind):
	res = 0
	for i in range(3):
		res += a[i][ind]
	return res

def getColumn(a, ind):
	res = []
	for i in range(3):
		res.append(a[i][ind])
	return res

def printMatrix(a):
	for i in range(3):
		for j in range(3):
			print('{0:.3f}'.format(a[i][j]), end=" ")
		print()


P = [[0.1, 0.12, 0.03],
	[0.11, 0.1, 0.11],
	[0.02, 0.31, 0.1]]

# P = [[0.25, 0, 0.125],
# 	[0.125, 0.25, 0.125],
# 	[0, 0.0625, 0.0625]]
px = [0]*3
py = [0]*3

allP = []
for row in P:
	for x in row:
		allP.append(x)
print(sum(allP))
for i in range(3):
	for j in range(3):
		px[i] += P[i][j]
		py[j] += P[i][j]


for i in range(3):
	print("p(x",i+1, ") = ", px[i])
print()
for i in range(3):
	print("p(y",i+1, ") = ", py[i])

print("-----------------------")

print("H(x) = ", Entropia(px))
print("H(y) = ", Entropia(py))
print("-----------------------")


print("ro(x) = ", Nadl(Entropia(px), len(px)))
print("ro(y) = ", Nadl(Entropia(py), len(py)))
print("-----------------------")
print(allP)
print("H(X,Y) = ", Entropia(allP))
print("-----------------------")


print("I(X i Y) = H(X) + H(Y) - H(X, Y) = ", Entropia(px) + Entropia(py) - Entropia(allP))
print("-----------------------")

print("Матриця умовних ймовірностей P(X|Y)")

rowSums = []
for i in range(3):
	rowSums.append(rowSum(P, i))
colSums = []
for i in range(3):
	colSums.append(colSum(P, i))

PXY = []
PYX = []

for i in range(3):
	row1 = []
	row2 = []
	for j in range(3):
		row1.append(P[i][j] / colSums[j])
		row2.append(P[i][j] / rowSums[i])
	PXY.append(row1)
	PYX.append(row2)
printMatrix(PXY)
print("-----------------------")


for i in range(3):
	print("H(X|y", i+1, ") = ", Entropia(getColumn(PXY, i)))

HXY = 0
for i in range(3):
	HXY += Entropia(getColumn(PXY, i)) * colSum(P, i)

print("H(X|Y) = ", HXY)

print("--------------------")

print("Матриця умовних ймовірностей P(Y|X)")
printMatrix(PYX)
print("-----------------------")


for i in range(3):
	print("H(Y|x", i+1, ") = ", Entropia(PYX[i]))

HYX = 0
for i in range(3):
	HYX += Entropia(PYX[i]) * rowSum(P, i)

print("H(Y|X) = ", HYX)


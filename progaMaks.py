a = list(map(int, input().split()))
if len(a) % 2 == 1:
	print("wrong input")
	exit(0)

n = len(a) // 2
print(a[:n])
print(a[n:])
print("---------------")
for i in range(n):
	if a[i] < a[n+i]:
		a[i], a[n+i] = a[n+i], a[i]

print(a[:n])
print(a[n:])
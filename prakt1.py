import math

print("input x, m, eps")
x, m, EPS = map(float, input().split())

if (EPS<0):
	exit(0)

res = 1
i = 1
cur_elem = x*m
last_elem = 0
while abs(cur_elem - last_elem)>EPS:
	res += cur_elem
	last_elem = cur_elem
	i+=1
	cur_elem *= m-i+1
	cur_elem /= i
	cur_elem *= x

print(res)
print((1+x)**m)
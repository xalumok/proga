def merge(s, l, m, r):
	left = []
	right = []
	for i in range(l, m+1):
		left.append(s[i])
	for i in range (m+1, r+1):
		right.append(s[i])

	i = 0 
	j = 0
	mergedArr = []
	while i<len(left) and j<len(right):
		if (left[i] <= right[j]):
			mergedArr.append(left[i])
			i += 1
		else:
			mergedArr.append(right[j])
			j += 1

	while i<len(left):
		mergedArr.append(left[i])
		i += 1
	while j<len(right):
		mergedArr.append(right[j])
		j += 1
	for i in range(len(mergedArr)):
		s[i+l] = mergedArr[i]


def mergeSort(s, l ,r):
	if r>l:
		m = (l+r)//2
		mergeSort(s, l, m)
		mergeSort(s, m+1, r)
		merge(s, l, m ,r)


def areAnagrams(s1, s2):
	s1 = list(s1)
	s2 = list(s2)
	if len(s1)!=len(s2):
		return False
	
	mergeSort(s1, 0, len(s1)-1)
	mergeSort(s2, 0, len(s2)-1)
	
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			return False

	return True



s1 = input()
s2 = input()

print(areAnagrams(s1,s2))


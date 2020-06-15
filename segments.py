def points(n, a, b, c):
	arrStart = find_points(n, a, True)
	arrEnd = find_points(n, b, False)
	return find_parts(arrStart, arrEnd, c, n)
	


def find_points(n, distance, is_start):
	a = 0
	b = n
	checker = 1
	if not is_start:
		a = n
		b = 0
		distance *= -1
		checker = -1
	ans = []
	for i in range(a, b + checker, distance):
		ans.append(i)
	return ans

def find_parts(arr1, arr2, distance, length):
	basearr = []
	for n in arr1:
		basearr.append(n)
	for m in arr2:
		basearr.append(m)
	basearr.sort()
	for i in range(len(basearr) - 1):
		if(abs(basearr[i] - basearr[i + 1]) == distance):
			length -= distance
	return length

if __name__ == '__main__':
	inputs = map(int, input().split())
	print(points(*inputs))
	

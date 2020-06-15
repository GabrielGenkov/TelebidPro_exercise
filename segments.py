class Point():
	def __init__(self, n, a, b, c):
		self.n = n
		self.a = a
		self.b = b
		self.c = c 	
	
	def points(self):
		arrStart = self.__find_points(self.a, True)
		arrEnd = self.__find_points(self.b, False)
		return self.__calculate(self.__find_parts(arrStart, arrEnd), self.c, self.n)

	
	def __find_points(self, distance, is_start):
		a = 0
		b = self.n
		checker = 1
		if not is_start:
			a = self.n
			b = 0
			distance *= -1
			checker = -1
		ans = []
		for i in range(a, b + checker, distance):
			ans.append(i)
		return ans
	
	@staticmethod
	def __find_parts(arr1, arr2):
		basearr = []
		for n in arr1:
			basearr.append(n)
		for m in arr2:
			basearr.append(m)
		basearr.sort()
		basearr = set(basearr)
		basearr = list(basearr)
		return basearr
		
		
	@staticmethod
	def __calculate(arr, distance, length):
		parts = []
		for i in range(len(arr) - 1):
			for j in range(i, len(arr)):
				if(abs(arr[i] - arr[j]) == distance):
					length -= distance
					parts.append((arr[i], arr[j]))
		return length, parts

if __name__ == '__main__':
	inputs = map(int, input().split())
	print(Point(*inputs).points()[0])

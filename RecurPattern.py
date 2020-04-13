from sys import argv
def recursivepattern(var, matrix, n=1):
	temp = str([str(i) for i in matrix])
	nor = len(matrix)//2
	for i in range(nor - var, nor + var+1):
		for j in range(nor - var, nor + var+1):
			if abs(i-nor) + abs(j-nor) >= var:
				matrix[i][j] = '+'
			else:
				matrix[i][j] = ' '
	print(n)
	if temp == str([str(i) for i in matrix]):
		return matrix
	else:
		recursivepattern(var//2, matrix, n+1)


if __name__ == '__main__':
	n = int(argv[1])
	matrix = [[' ' for i in range(2**n+1)] for j in range(2**n+1)]
	pattern = recursivepattern(2**(n-1), matrix)
    print(pattern)
	for i in pattern:
		for j in i:
			print(j, end=" ")
		print("")

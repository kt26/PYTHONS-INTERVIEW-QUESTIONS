n = int(input())
a = [ [0]*n  for i in range(n) ]

up = left = 0
right = down = n
counter = 1

while (up<=down and up<=right):

	for i in range(up,right):
		a[up][i] = counter
		counter+=1

	up=up+1

	for i in range(up,down):
		a[i][right-1] = counter
		counter+=1

	right=right-1


	for i in range(right-1,left-1,-1):
		a[down-1][i] = counter
		counter+=1

	down=down-1


	for i in range(down-1,up-1,-1):
		a[i][left] = counter
		counter+=1

	left=left+1


print(a)


















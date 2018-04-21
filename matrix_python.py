def arr(lst,r,c):
	sr_val = 0
	for i in range(len(lst)):
		arr_val = lst[i].count(sr_val)
		if (arr_val > 0):
			l_index = lst[i].index(sr_val)
			lst[i] = [0 for x in range(c)]
	
	for i in range(len(lst)):
		lst[i][l_index]=0

	print(arr_val)
	print(lst)

matrix = []
print("Enter the desired combination (rows, columns): ")
r,c = input().split(",")
r,c = [int(r),int(c)]
for i in range(r):
	row_val=[]
	print("Enter "+str(c)+" values")
	for i in range(c):
		row_val.append(int(input()))
	matrix.append(row_val)

arr(matrix,r,c)

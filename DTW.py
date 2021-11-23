def normalize(arr):
	out = []
	min_in_arr = min(arr)
	max_in_arr = max(arr)

	for item in arr:
		out.append(((item-min_in_arr)/max_in_arr)*100)
	return out


def dist(x, y):
	return abs(x-y)


def Data_Time_Warping(arr1, arr2):
	out = []
	data_table = []
	for i in range(len(arr1)):
		data_table.append([])
		for j in range(len(arr2)):
			data_table[i].append(dist(arr1[i], arr2[j]))
	
	for i in range(1, len(arr1)):
		data_table[i][0] += data_table[i-1][0]

	for j in range(1, len(arr2)):
		data_table[0][j] += data_table[0][j-1]

	for i in range(1, len(arr1)):
		for j in range(1, len(arr2)):
			data_table[i][j] += min(data_table[i-1][j-1], min(data_table[i-1][j], data_table[i][j-1]))

	i = len(arr1)-1
	j = len(arr2)-1

	out.append((i, j))

	while i+j != 0:
		if (i == 0):
			j -= 1
			out.append((i, j))
		elif (j == 0):
			i -= 1
			out.append((i, j))
		else:
			_min = 0
			way = (0, 0)
			if (data_table[i-1][j-1] <= data_table[i-1][j]):
				_min = data_table[i-1][j-1]
				way = (-1, -1)
			else:
				_min = data_table[i-1][j]
				way = (-1, 0)
			if (data_table[i][j-1] <= _min):
				_min = data_table[i][j-1]
				way = (0, -1)
			i, j = i + way[0], j + way[1]
			out.append((i, j))
	return out, data_table[len(arr1)-1][len(arr2)-1]


def Restore_path(path, arr1, arr2):
	out = []
	for item in path:
		out.append((arr1[item[0]], arr2[item[1]]))
	return out


def Format_data_for_Excel(graph):
	for i in range(len(graph)-1, -1, -1):
		print(str(graph[i][0]).replace('.',','))
	print()
	for i in range(len(graph)-1, -1, -1):
		print(str(graph[i][1]).replace('.',','))


def Format_path_to_table(path, n, m):
	for i in range(-1, n):
		for j in range(-1, m):
			if (i == -1):
				if (j == -1):
					print('+', end = '')
				else:
					print('|', end = '')
			else:
				if (j == -1):
					print('-', end = '')
				else:
					if ((i, j) in path):
						print('#', end = '')
					else:
						print(' ', end = '')
		if (i != n):
			print()


n, m = map(int, input().split())
first_data_time = list(map(float, input().split()))
second_data_time = list(map(float, input().split()))

nomr_first_data_time = normalize(first_data_time)
nomr_second_data_time = normalize(second_data_time)

DTW_result, dist = Data_Time_Warping(nomr_first_data_time, nomr_second_data_time)

graph = Restore_path(DTW_result, first_data_time, second_data_time)

print('--Distance--')
print(dist)
print('----')
print('--Data formated for graph in Excel--')
Format_data_for_Excel(graph)
print('----')
print('--Visualization of path--')
Format_path_to_table(DTW_result, len(first_data_time), len(second_data_time))
print('----')

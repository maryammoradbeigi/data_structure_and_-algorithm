# Selection Search: Complexity = n^2
def selection_sort(lst):
	for idx in range(len(lst)):
		min_idx = idx

		for i in range(idx+1, len(lst)):
			if lst[i] < lst[min_idx]:
				min_idx = i
		lst[min_idx], lst[idx] = lst[idx], lst[min_idx]
		




def insertion_sort_desc(lst):
	for idx in range(1, len(lst)):
		val = lst[idx]
		position = idx

		while position > 0 and val >lst[position-1]:
			lst[position] = lst[position-1]
			position -= 1
		lst[position] = val

def insertion_sort_asc(lst):
	for idx in range(1, len(lst)):
		val = lst[idx]
		position = idx

		while position > 0 and val < lst[position-1]:
			lst[position] = lst[position-1]
			position -= 1
		lst[position] = val

def bubble_sort(lst):
	is_sorted = False
	i = 0
	while i < len(lst) and not is_sorted:
		is_sorted = True
		for position in range(len(lst)-1-i):
			if lst[position] > lst[position+1]:
				lst[position], lst[position+1]= lst[position+1], lst[position]
				is_sorted = False
		i +=1
		

# Test
# lst = [100, 1, 2, 5, 15, 10, 8, 4, 21]
lst =[1,2,3,4,5,6]
bubble_sort(lst)
print(lst)

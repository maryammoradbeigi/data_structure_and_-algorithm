import random
# Sequential Search
# Resource: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSequentialSearch.html

## My solution
def sequential_search(lst, num):
	item_index = 0
	while item_index < len(lst):
		if lst[item_index] == num:
			return item_index
		item_index += 1
	return -1
			


## Solution on the Internet
def Sequential_Search(dlist, item):
    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos



# Binary Search
# Resource: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html

## My solution
def binary_search(lst, key):
	start=0
	end=len(lst)-1
	while start < end:
		position = (start+end)//2
		print([start, end, position])
		if lst[position]==key:
			return position
		elif lst[position] < key:
			start = position + 1
		else:
			end = position - 1
	return -1

def test():
	l=[_ for _ in range(100000)]

	print(binary_search(l, 96))

# # Solution in the interner
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False

#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
# 	        else:
# 	            if item < alist[midpoint]:
# 	                last = midpoint-1
# 	            else:
# 	                first = midpoint+1
#     return found

if  __name__ == "__main__":
	test()
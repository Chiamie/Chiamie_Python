def mergeList(list1, list2):
	for number in list2:
		list1.append(number)
	return list1
	
def getMedian(list1, list2):
	result = mergeList(list1, list2)
	print(result)
	result = sorted(result)
	print(result)
	if len(result) % 2 == 0:
		median = ((len(result) / 2) + ((len(result) + 2) / 2)) / 2
	else:
		median = ((len(result) + 1)/2)
	return median
		
			
		
nums1 = [1, 3]
nums2 = [2]

print(getMedian(nums1, nums2))

age1= [1,2]
age2 = [3,4]

print(getMedian(age1, age2))

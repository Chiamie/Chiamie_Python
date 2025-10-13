def mergeList(list1, list2):
	for number in list2:
		list1.append(number)
	return list1
	
def getAverage(list1, list2):
	result = mergeList(list1, list2)
	sum = 0
	for number in result:
		sum += number
	return sum / len(result)
	
		
nums1 = [1, 3]
nums2 = [2]

print(getAverage(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]

print(getAverage(nums1, nums2))
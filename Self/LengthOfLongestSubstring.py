def get_all_sub_strings(word):
    list_of_subString = []
    for index in range(len(word)):
        subString = ""
        for counter in range(index, len(word)):
            if word[counter] not in subString:
                subString += word[counter]
            else:
                break
        list_of_subString.append(subString)
    return list_of_subString


def get_highest_subString(words):
	largest = words[0]
	for element in words:
		if len(element) > len(largest):
			largest = element
	return len(largest)
		
s = "abcabcdabb"
result = get_all_sub_strings(s)
print(get_highest_subString(result))

s = "bbbbb"
result = get_all_sub_strings(s)
print(get_highest_subString(result))

s = "pwwkew"
result = get_all_sub_strings(s)
print(get_highest_subString(result))






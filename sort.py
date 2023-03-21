def sort_dictionary(dictionary):
	dictionary_order = sorted(dictionary.items(), key = lambda x: x[1][1])
	dictionary_output = [(name, element[0]) for name, (phone_num, age) in dictionary_order]
	return dictionary_output


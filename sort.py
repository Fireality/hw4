def sort_dictionary(dictionary):
	dictionary_order = sorted(dictionary.items(), key = lambda x: x[1][1], reverse = True)
	dictionary_output = [(i, element[0]) for i, element in dictionary_order]
	return dictionary_output


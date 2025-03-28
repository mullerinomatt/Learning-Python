def reverse_dict_of_lists(input_dict):
    """Reverses a dictionary where values are lists."""
    reversed_dict = {}
    for key, value_list in input_dict.items():
        for value in value_list:
            if value not in reversed_dict:
                reversed_dict[value] = []
            reversed_dict[value].append(key)
    return reversed_dict
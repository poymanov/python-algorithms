def binary_search(needle, haystack):
    min_index = 0
    max_index = len(haystack) - 1

    while not min_index == max_index:
        compared_index = (min_index + max_index) // 2

        if needle == haystack[compared_index]:
            return compared_index
        elif needle < haystack[compared_index]:
            max_index = compared_index
        else:
            min_index = compared_index + 1

    return None

def find_max(number_list):
    try:
        max_number = number_list[0]
        for i in number_list:
            if max_number < i:
                max_number = i
        return max_number
    except TypeError:
        print('You did not input a list')

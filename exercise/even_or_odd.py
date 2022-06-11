def even_odd(*args):
    type_of_number = args[-1]
    result = []
    difference = 0 if type_of_number == "even" else 1
    for num_index in range(len(args) - 1):
        if args[num_index] % 2 == difference:
            current_num = args[num_index]
            result.append(current_num)

    return result


print(even_odd((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd")))
def words_sorting(*args):
    words_values = {}
    sum_of_values = 0
    for word in args:
        if word not in words_values:
            words_values[word] = 0
        for char in word:
            words_values[word] += ord(char)
            sum_of_values += ord(char)
    if sum_of_values % 2 == 0:
        sorted_dict = sorted(words_values.items(), key=lambda x: x[0])
    else:
        sorted_dict = sorted(words_values.items(), key=lambda x: x[1], reverse=True)

    result = [f"{word} - {num}" for word, num in sorted_dict]

    return '\n'.join(result)


print(words_sorting('escape', 'charm', 'eye'))
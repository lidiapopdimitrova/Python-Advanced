def even_odd_filter(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if key == "even":
            new_dict["even"] = [x for x in value if x % 2 == 0]
        else:
            new_dict["odd"] = [x for x in value if x % 2 != 0]

    sort_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    result = {}
    for k, v in sort_dict:
        result[k] = v

    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

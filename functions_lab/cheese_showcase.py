def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(),
                         key=lambda x: (-len(x[1]), x[0]))

    result = []

    for name, pieces in sorted_dict:
        result.append(name)
        new_pieces = sorted(pieces, reverse=True)
        for value in new_pieces:
            result.append(value)

    return "\n\r".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

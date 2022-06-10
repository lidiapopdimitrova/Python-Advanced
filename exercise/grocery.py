def grocery_store(**kwargs):
    sorted_receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = [f"{product}: {quantity}" for product, quantity in sorted_receipt]

    return "\n".join(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

def shopping_cart(*args):
    meal_dict = {}
    current_command = 0
    for command in args:

        if command != "Stop":
            meal = args[current_command][0]
            product = args[current_command][1]
            if meal not in meal_dict:
                meal_dict[meal] = []
                meal_dict[meal].append(product)
                current_command += 1
            else:
                if meal == "Pizza":
                    if len(meal_dict[meal]) >= 4:
                        break
                    elif product not in meal_dict[meal]:
                        meal_dict[meal].append(product)
                elif meal == "Soup":
                    if len(meal_dict[meal]) >= 3:
                        break
                    elif product not in meal_dict[meal]:
                        meal_dict[meal].append(product)
                elif meal == "Dessert":
                    if len(meal_dict[meal]) >= 2:
                        break
                    elif product not in meal_dict[meal]:
                        meal_dict[meal].append(product)
                current_command += 1

            if "Soup" not in meal_dict:
                meal_dict["Soup"] = []
            if "Dessert" not in meal_dict:
                meal_dict["Dessert"] = []
            if "Pizza" not in meal_dict:
                meal_dict["Pizza"] = []
        else:
            break

    if not meal_dict:
        return "No products in the cart!"
    else:

        sorted_meals = sorted(meal_dict.items(), key=lambda x: (-len(x[1]), x[0]))
        final = []
        for name, product in sorted_meals:
            final.append(f"{name}:")

            for p in sorted(product):
                final.append(f" - {p}")

    return "\n".join(final)


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


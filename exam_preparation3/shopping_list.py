def shopping_list(budget, **kwargs):
    types_of_products = 0
    bought_products = {}
    if budget >= 100:

        for product_name, tuples in kwargs.items():

            price, quantity = tuples
            if price * quantity <= budget:
                budget -= price * quantity
                if product_name not in bought_products:
                    bought_products[product_name] = price * quantity
                    types_of_products += 1
                else:
                    bought_products[product_name] = price * quantity
                if types_of_products >= 5:
                    break

    else:
        return "You do not have enough budget."
    final_result = [f"You bought {products} for {prices:.2f} leva." for products, prices in bought_products.items()]
    return "\n".join(final_result)


# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
def age_assignment(*args, **kwargs):
    results = {}
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                results[name] = age

    sorted_dict = sorted(results.items(), key=lambda x: x[0])
    final_result = [f"{names} is {ages} years old." for names, ages in sorted_dict]
    return "\n".join(final_result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
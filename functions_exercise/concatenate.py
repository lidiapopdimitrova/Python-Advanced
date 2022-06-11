def concatenate(*args, **kwargs):
    text = ""
    for letters in args:
        text += letters

    for key, value in kwargs.items():
        if key in text:

            text = text.replace(key, value)
    return text


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
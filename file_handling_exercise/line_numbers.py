import string


def count_letters(text):
    letter_count = 0
    for letter in text:
        if letter.isalpha():
            letter_count += 1
    return letter_count


def count_symbols(text):
    symbol_count = 0
    for letter in text:
        if letter in string.punctuation:
            symbol_count += 1
    return symbol_count


with open("./text.txt", "r") as file:
    for idx, line in enumerate(file):
        print(f"Line {idx + 1}: {line.strip()} ({count_letters(line)}) ({count_symbols(line)})")
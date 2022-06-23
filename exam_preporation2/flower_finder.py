from collections import deque

word1 = "rose"
word2 = "tulip"
word3 = "lotus"
word4 = "daffodil"

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

is_found_word1 = False
is_found_word2 = False
is_found_word3 = False
is_found_word4 = False

while vowels and consonants:

    first_vowel = vowels.popleft()
    first_consonant = consonants.pop()

    for char in word1:
        if char == first_vowel:
            word1 = word1.replace(char, "")
        if char == first_consonant:
            word1 = word1.replace(char, "")
    if not word1:
        is_found_word1 = True
        break

    for char in word2:
        if char == first_vowel:
            word2 = word2.replace(char, '')
        if char == first_consonant:
            word2 = word2.replace(char, '')
    if not word2:
        is_found_word2 = True
        break

    for char in word3:
        if char == first_vowel:
            word3 = word3.replace(char, '')
        if char == first_consonant:
            word3 = word3.replace(char, '')
    if not word3:
        is_found_word3 = True
        break

    for char in word4:
        if char == first_vowel:
            word4 = word4.replace(char, '')
        if char == first_consonant:
            word4 = word4.replace(char, '')
    if not word4:
        is_found_word4 = True
        break


if is_found_word1:
    print(f"Word found: rose")
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")
elif is_found_word2:
    print(f"Word found: tulip")
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")
elif is_found_word3:
    print(f"Word found: lotus")
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")
elif is_found_word4:
    print(f"Word found: daffodil")
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")
else:
    print("Cannot find any word!")
    if vowels:
        print(f"Vowels left: {' '.join(x for x in vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(x for x in consonants)}")


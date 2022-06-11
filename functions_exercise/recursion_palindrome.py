def palindrome(word, index):
    if index == len(word) - 1:
        return f"{word} is a palindrome"

    if word[index] == word[-index - 1]:
        index += 1
        return palindrome(word, index)
    else:
        return f"{word} is not a palindrome"


print(palindrome("peter", 0))
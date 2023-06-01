def is_palindrome_iterative(word):
    if not word:
        return False

    word_size = len(word)

    for index in range(word_size // 2):
        if word[index] != word[word_size - index - 1]:
            return False

    return True

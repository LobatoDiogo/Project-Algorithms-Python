def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    if not arr:
        return []

    pivot = arr[len(arr) // 2]
    lesser = [char for char in arr if char < pivot]
    equal = [char for char in arr if char == pivot]
    greater = [char for char in arr if char > pivot]

    return quick_sort(lesser) + equal + quick_sort(greater)


def is_anagram(first_string, second_string):
    word1_low = first_string.lower()
    word2_low = second_string.lower()

    if not word1_low and not word2_low:
        return (word1_low, word2_low, False)

    first_word = quick_sort(list(word1_low))
    second_word = quick_sort(list(word2_low))

    are_anagrams = first_word == second_word

    return ("".join(first_word), "".join(second_word), are_anagrams)

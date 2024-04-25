def longest_word(words):
    longest_word = " "
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word, max_length
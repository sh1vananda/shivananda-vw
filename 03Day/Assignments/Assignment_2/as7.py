def filter_long_words(words, l):
    long_words = []
    for word in words:
        if len(word) > l:
            long_words.append(word)
    return long_words

print(filter_long_words(["abc", "defg", "ghi", "jklm"], 3))
def find_longest_word(words):
    curr_max = float('-inf')
    curr_word = ""
    for word in words:
        l = len(word)
        if l > curr_max:
            curr_max = l
            curr_word = word
    return curr_word, curr_max

words = list(input().split())

# w = max(words, key=len)
# l = len(w)

w, l = find_longest_word(words)

print(f"longest word is {w} with length {l}")
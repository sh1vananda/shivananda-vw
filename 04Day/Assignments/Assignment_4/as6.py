def count(words):
    d = {}

    for word in words:
        for letter in word:
            if letter.isalnum():
                if letter in d:
                    d[letter] += 1
                else:
                    d[letter] = 1
    
    return sorted(d.items())

text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."
words = text.lower().split()

print(count(words))

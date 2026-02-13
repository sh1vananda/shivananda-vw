vowels = ["a", "e", "i", "o", "u"]

def encode(text):
    text_list = text.split()
    encoded = ""
    for word in text_list:
        for letter in word:
            if letter not in vowels:
                encoded += letter + "o" + letter
            else:
                encoded += letter
        encoded += " "
    return encoded

print(encode("this is fun"))
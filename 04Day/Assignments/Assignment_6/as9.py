def even(text):
    even_positions = ""
    for i in range(len(text)):
        if (i+1) % 2 == 0: # or just i if considering count from 0
            even_positions += text[i]
    return even_positions 

def odd(text):
    odd_positions = ""
    for i in range(len(text)):
        if (i+1) % 2 != 0: # again, just i if considering count from 0
            odd_positions += text[i]
    return odd_positions 

def append_a(text):
    return text + "".join(["a"]*len(text))

print("A. characters at even positions\nB. characters at odd positions\nC. length of the text\nD. append 'a's")
choice = input("choice (A, B, C, D): ")
text = input("enter text: ")

match choice:
    case "A":
        print(f"characters in even positions: {even(text)}")
    case "B":
        print(f"characters in odd positions: {odd(text)}")
    case "C":
        print(f"length of text: {len(text)}")
    case "D":
        print(f"appended 'a's: {append_a(text)}")
    case _:
        print("invalid choice")

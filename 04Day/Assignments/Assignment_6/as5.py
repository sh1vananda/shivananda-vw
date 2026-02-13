def alter(text):
    # return text.replace("this", "that")

    text_list = text.split()
    for i, word in enumerate(text_list):
        if word == "this":
            text_list[i] = "that"
    return " ".join(text_list)


print(alter("this is me and this is my python program"))
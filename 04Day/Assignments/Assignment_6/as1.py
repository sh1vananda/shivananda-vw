key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P',
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C',
'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

characters = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]

def encode_decode(text):
    text_list = text.split()
    altered = ""
    for word in text_list:
        for letter in word:
            if letter.isalnum():
                altered += key[letter]
            else:
                altered += letter
        altered += " "
    return altered

cypher_text = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
normal_text = "Caesar cipher? I much prefer Caesar salad!"

print(encode_decode(cypher_text))
print(encode_decode(normal_text))
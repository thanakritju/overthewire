from collections import defaultdict


encrypted = 'KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS'

with open("level4/found1.txt", "r") as f:
    found1 = f.read()

with open("level4/found2.txt", "r") as f:
    found2 = f.read()

with open("level4/found3.txt", "r") as f:
    found3 = f.read()

text = f"{found1}{found2}{found3}".replace(" ", "")

# Analysis

fequency = defaultdict(int)
bigram = defaultdict(int)
trigram = defaultdict(int)

for char in text:
    fequency[char] = fequency[char] + 1

for i in range(1, len(text)):
    bigram[text[i-1]+text[i]] = bigram[text[i-1]+text[i]] + 1

for i in range(1, len(text)):
    trigram[text[i-2]+text[i-1]+text[i]
            ] = trigram[text[i-2]+text[i-1]+text[i]] + 1

# print("single", sorted(fequency.items(), key=lambda kv: kv[1])[-10:])
# print("bigram", sorted(bigram.items(), key=lambda kv: kv[1])[-10:])
# print("trigram", sorted(trigram.items(), key=lambda kv: kv[1])[-10:])

# substitution

key = {
    'S': 'e',
    'D': 'h',
    'J': 't',
    'N': 'r',
    'Q': 'a',
    'G': 'n',
    'W': 'd',
    'U': 's',
    'Z': 'c',
    'L': 'y',
    'Y': 'p',
    'V': 'l',
    'C': 'i',
    'B': 'o',
    'E': 'g',
    'X': 'f',
    'H': 'q',
    'M': 'u',
    'A': 'b',
    'K': 'w',
    'R': 'j',
    'T': 'm',
    'I': 'v'
}

decrypted_text = ""

for char in encrypted.replace(" ", ""):
    if char in key:
        decrypted_text += key[char]
    else:
        decrypted_text += char

print(decrypted_text)

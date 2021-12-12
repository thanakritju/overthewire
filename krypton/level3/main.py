from string import ascii_uppercase


encrypted = 'OMQEMDUEQMEK'
rotation = 12
answer = ""

for char in encrypted:
    if char == " ":
        answer += " "
    else:
        new_index = (ascii_uppercase.index(char) - rotation) % 26
        answer += ascii_uppercase[new_index]

print(answer)





# rule for giraffe language -> any vowel gets converted to "g"

# METHOD 1
caps_vowels = ["A", "E", "I", "O", "U"]
Lower_vowels = ["a", "e", "i", "o", "u"]

translation = ""

word = input("Enter text: ")
index = 0
# print(word[index])
# for letter in word:
#     print(letter)
#     if letter in vowels:
#         word[index] = "g"    -> individal string letters cant be modified, property of strings.
#     print(letter)
#     index += 1

for letter in word:
    if letter in caps_vowels:  # OR if letter in 'aeiouAEIOU'
        translation += "G"  # appending g to translation if vowel
    elif letter in Lower_vowels:
        translation += "g"
    else:
        translation += letter


print("translation:", translation)

# METHOD 2


def translate(phrase):
    output = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                output += "G"
            else:
                output += "g"
        else:
            output += letter
    return output


print(translate(input("Enter string to be translated: ")))

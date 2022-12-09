print("Hello world")
# x = float(input("Enter a number you want: "))
# print(x / 2)

phrase = "VERNON DUdLEY"

print(phrase.isupper())
phrase = phrase.upper()
print(phrase.isupper())
print(phrase)
y = len("hello" + phrase)  # measures the length, space character also included
print(y)

print(phrase.index("N"))  # returns index of first occurance of N in phrase

print(
    phrase.index("DUD")
)  # like ctrl+F in windows, returns index where this string starts in phrase

print(phrase.replace("VERNoN", "Petunia"))  # replaces vernon by petunia, case sensative

# many others can be found through basic google search

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

month_code = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
    # 1: "January",
    # 2: "February",   keys value pair can be of any data type.
}

month = input("Enter any month: ")

print(month_code[month.lower()])

print(
    month_code.get("may", "Not a valid key sorry")
)  # -> prints not a valid key if key does not match any input.

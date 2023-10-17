def is_pallindrome(s):
    s = s.replace(" ","").lower()

    return s == s[::-1]

test_strings = [
    "malayalam",
    "radar",
    "level",
    "apple",
    "google",
]

for string in test_strings:
    if is_pallindrome(string):
        print(f"{string} is a pallindrome.")
    else:
        print(f"{string} is NOT a pallindrome")
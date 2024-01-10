symbols = "*/=+%@#&$"
digits = "0123456789"

text = open("input.txt").read()
text = ".........123/12&..."
text_width = len(text.split("\n")[0])

current_number = ""
should_add = False
parts_sum = 0

for i in range(0, len(text)):
    mid = text[i]
    top = "." if i > text_width else text[i - text_width]
    bottom = "." if i < text_width else text[i + text_width]

    if mid in digits: current_number += mid
    elif mid in symbols:
        should_add = True
        if not current_number == "":
            parts_sum += int(current_number)
            current_number = ""
    else:
        if should_add: parts_sum += int(current_number)
        current_number = ""
        should_add = False

print(parts_sum)

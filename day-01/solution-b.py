lines = open("input.txt").read().split("\n")[:-1]

literal_digits = { d: str(n + 1)  for n, d in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}
numeral_digits = { str(n): str(n)  for n in range(1, 10)}
digits_table = literal_digits | numeral_digits
digits = list(digits_table)

def get_calibration_value(line):
    left = "0"
    right = "0"

    for i in range(0, len(line)):
        current = ""

        for j in range(i, len(line)):
            current += line[j]

            if current in digits:
                if left == "0": left = digits_table[current]
                right = digits_table[current]
                i += len(right)
                break


    return int(left + right)

solution = sum([get_calibration_value(line) for line in lines])
open("output-b.txt", mode="w").write(str(solution))

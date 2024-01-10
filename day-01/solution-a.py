lines = open("input.txt").read().split("\n")[:-1]

digits = [str(n) for n in range(0, 10)]

def get_calibration_value(line):
    first = "0"
    last = "0"
    
    for char in line:
        if char in digits and first == "0":
            first = char
            last = char
        elif char in digits: last = char

    return int(first + last)

solution = sum([get_calibration_value(line) for line in lines])
open("output-a.txt", mode="w").write(str(solution))

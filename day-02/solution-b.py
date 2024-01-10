def calc_game_score(line):
    [game_data, raw_data] = line.split(":")
    ID = int(game_data.split(" ")[1])
    sets = [s.strip() for s in raw_data.split(";")]

    min_red = 0
    min_green = 0
    min_blue = 0

    for s in sets:
        raw_elements = [e.strip() for e in s.split(",")]
        elements = [(e.split(" ")[1], int(e.split(" ")[0])) for e in raw_elements]
        
        red = sum([v for c, v in elements if c == "red"])
        green = sum([v for c, v in elements if c == "green"])
        blue = sum([v for c, v in elements if c == "blue"])

        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)

    return min_red * min_green * min_blue

lines = open("input.txt").read().split("\n")
solution = sum([calc_game_score(line) for line in lines])
open("output-b.txt", mode="w").write(str(solution))
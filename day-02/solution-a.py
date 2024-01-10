def calc_game_score(line):
    [game_data, raw_data] = line.split(":")
    ID = int(game_data.split(" ")[1])
    sets = [s.strip() for s in raw_data.split(";")]

    for s in sets:
        raw_elements = [e.strip() for e in s.split(",")]
        elements = [(e.split(" ")[1], int(e.split(" ")[0])) for e in raw_elements]
        
        red = sum([v for c, v in elements if c == "red"])
        green = sum([v for c, v in elements if c == "green"])
        blue = sum([v for c, v in elements if c == "blue"])

        if red > 12: return 0
        if green > 13: return 0
        if blue > 14: return 0
    
    return ID

lines = open("input.txt").read().split("\n")
solution = sum([calc_game_score(line) for line in lines])
open("output-a.txt", mode="w").write(str(solution))
lines = open(C:/Users/Benjy/Dropbox/Python/"input.txt").read().splitlines()

planets = ["Omicron", "Hoth", "Ryza", "Htrae"]

rate_text = lambda text: sum(c.isalpha() or c.isspace() for c in text)

for line in lines:
    line = line.split()
    results = [
        "".join(chr(int(c) ^ 0b10000) for c in line),
        "".join(chr(int(c) - 10) for c in line),
        "".join(chr(int(c) + 1) for c in line),
        "".join(chr(int(c)) for c in reversed(line))
    ]
    best = max(results, key=rate_text)
    planet = planets[results.index(best)]
    print("{:>7} | {}".format(planet, best))
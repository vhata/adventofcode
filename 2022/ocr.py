# Borrowed from @Atlante45

ALPHABET = {
    ".##.\n#..#\n#..#\n####\n#..#\n#..#": "A",
    "###.\n#..#\n###.\n#..#\n#..#\n###.": "B",
    ".##.\n#..#\n#...\n#...\n#..#\n.##.": "C",
    "####\n#...\n###.\n#...\n#...\n####": "E",
    "####\n#...\n###.\n#...\n#...\n#...": "F",
    ".##.\n#..#\n#...\n#.##\n#..#\n.###": "G",
    "#..#\n#..#\n####\n#..#\n#..#\n#..#": "H",
    "###.\n.#..\n.#..\n.#..\n.#..\n###.": "I",
    "..##\n...#\n...#\n...#\n#..#\n.##.": "J",
    "#..#\n#.#.\n##..\n#.#.\n#.#.\n#..#": "K",
    "#...\n#...\n#...\n#...\n#...\n####": "L",
    ".##.\n#..#\n#..#\n#..#\n#..#\n.##.": "O",
    "###.\n#..#\n#..#\n###.\n#...\n#...": "P",
    "###.\n#..#\n#..#\n###.\n#.#.\n#..#": "R",
    ".###\n#...\n#...\n.##.\n...#\n###.": "S",
    "#..#\n#..#\n#..#\n#..#\n#..#\n.##.": "U",
    "#...\n#...\n.#.#\n..#.\n..#.\n..#.": "Y",
    "####\n...#\n..#.\n.#..\n#...\n####": "Z",
}

EMPTY = "."
WIDTH = 4


def parse(drawing):
    lines = drawing.strip().splitlines()
    length = len(lines[0])

    result = ""

    index = 0
    while length - index >= WIDTH:
        skip = all(map(lambda line: line[index] == EMPTY, lines))
        if skip:
            index = index + 1
            continue
        letter = "\n".join(map(lambda line: line[index : index + WIDTH], lines))

        if letter not in ALPHABET:
            raise Exception("Error: unknown letter:\n", letter)

        result = result + ALPHABET[letter]

        index = index + 4
        # index += 5 if letter == "Y" else 4

    return result

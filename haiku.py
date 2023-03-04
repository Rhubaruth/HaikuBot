import random

syl1 = ["one", "dive", "kiss", "blue", "give"]
syl2 = ["purple", "driver", "silent", "aura"]
syl3 = ["parachute", "understand", "subdivide"]
syl4 = ["directory", "overwhelming", "termination", "avocado", "arugula"]
syl5 = ["geometrical", "terminology", "deconstruction"]
syl6 = ["disappriciated", "discontinuity"]
syl7 = ["naturopathically", "encyclopedia"]

SHORT = 5
LONG = 7


def create_line(length: int = 5) -> str:
    line = ""
    syllables = 0

    while syllables < length:
        word_syll = random.randint(1, length-syllables)
        syllables += word_syll

        match word_syll:
            case 1:
                random.shuffle(syl1)
                line += syl1[0]

            case 2:
                random.shuffle(syl2)
                line += syl2[0]

            case 3:
                random.shuffle(syl3)
                line += syl3[0]

            case 4:
                random.shuffle(syl4)
                line += syl4[0]

            case 5:
                random.shuffle(syl5)
                line += syl5[0]

            case 6:
                random.shuffle(syl6)
                line += syl6[0]

            case 7:
                random.shuffle(syl7)
                line += syl7[0]
        line += " "
    return line


def create_long():
    line = "LONG LINE"
    return line


def create_haiku() -> [str, str, str]:
    return [create_line(5), create_line(7), create_line(5)]


if __name__ == '__main__':
    print("Haiku time: ")
    haiku = create_haiku()
    print(*haiku, sep="\n")

import random
from nltk import CFG
from nltk.parse.generate import generate

haiku_grammar = CFG.fromstring("""
    START -> SHORT '$' LONG '$' SHORT
    SHORT -> \
        '1' '1' '1' '1' '1' | \
        '1' '1' '1' '2' | \
        '1' '1' '2' '1' | \
        '1' '2' '1' '1' | \
        '2' '1' '1' '1' | \
        '1' '2' '2' | \
        '2' '1' '2' | \
        '1' '2' '1' | \
        '1' '1' '3' | \
        '1' '3' '1' | \
        '3' '1' '1' | \
        '2' '3' | \
        '3' '2'
        
    LONG -> \
        SHORT '1' '1' |\
        SHORT '2' |\
        '1' '1' SHORT |\
        '2' SHORT |\
        '3' '3' '1' |\
        '3' '1' '3' |\
        '1' '3' '3'
    """)


def create_haiku():
    productions = generate(haiku_grammar, depth=5)
    rand_index = random.randint(0, sum(1 for _ in productions)-1)
    for product in generate(haiku_grammar, depth=5):
        if rand_index == 0:
            return ' '.join(product)
        rand_index -= 1
    return []


if __name__ == '__main__':
    print("Haiku time: ")
    haiku = [line.strip() for line in create_haiku().split('$')]
    print(*haiku, sep="\n")

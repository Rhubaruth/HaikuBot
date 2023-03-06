import random

import nltk
from nltk import CFG
from nltk.parse.generate import generate

haiku_grammar = CFG.fromstring("""
    START -> SHORT '$' LONG '$' SHORT
    SHORT -> \
        Adv2 Verb2 Pronoun1 | \
        Adj2 Noun3 | \
        Adj3 Noun2 | \
        Adj2 Adj2 Noun1 
        
    LONG -> \
        Adv3 Verb3 Noun1 | \
        Verb1 Noun1 ',' Verb1 Adj3 Pronoun1
    
    
    Noun1 -> 'car' | 'bar' | 'cup' | \
             'tea' | 'cat' | 'god' | \
             'dog' | 'snake' | 'crown'
    Noun2 -> 'bathtub' | 'rocket' | 'ticket' | \
            'victim' | 'goblin' | 'rabbit' | \
            'jacket' | 'cactus' | 'picnic'
    Noun3 -> 'orange' | 'family' | 'piano' | \
            'elephant' | 'cosmonaut' | 'radio' | \
            'revenge' | 'diamond' | 'history'
    
    Adj2 -> 'happy' | 'hungry' | 'alive' | \
            'lucky' | 'little' | 'ugly' | 'social'
    Adj3 -> 'flexible' | 'amusing' | 'forgetful' | \
            'determined' | 'ambitious' | 'romantic'
    
    Pronoun1 -> 'me' | 'her' | 'him' | 'them' | 'it'
    
    Verb1 -> 'drag' | 'bite' | \
            'give' | 'get' | 'steal'
    Verb3 -> 'overlook' | 'manufacture' | \
            'disenchant' | 'looking for'
    
    Adv2 -> 'sadly' | 'often'
    Adv3 -> 'quickly' | 'silently' | 'happily' | \
            'hopefully' | 'horribly'
    
    """)
SHORT = nltk.Nonterminal('SHORT')
LONG = nltk.Nonterminal('LONG')

SHORT_COUNT = sum(1 for _ in generate(haiku_grammar, start=SHORT, depth=4))-1
LONG_COUNT = sum(1 for _ in generate(haiku_grammar, start=LONG, depth=4))-1
# production_count = 8200850
print(SHORT_COUNT, LONG_COUNT, sep="   ")


def create_haiku() -> [str, str, str]:


    first_line_id = random.randint(0, SHORT_COUNT)
    second_line_id = random.randint(0, SHORT_COUNT)
    first_line = ""
    second_line = ""
    for product in generate(haiku_grammar, start=SHORT, depth=4):
        if first_line_id == 0:
            first_line = ' '.join(product)
        if second_line_id == 0:
            second_line = ' '.join(product)
        if first_line_id == 0 and second_line_id == 0:
            break
        first_line_id -= 1
        second_line_id -= 1

    long_line_id = random.randint(0, LONG_COUNT)
    for product in generate(haiku_grammar, start=LONG, depth=4):
        if long_line_id == 0:
            return [first_line, ' '.join(product), second_line]
        long_line_id -= 1

    return ""


if __name__ == '__main__':
    print("Haiku time: ")
    haiku = create_haiku()
    print(*haiku, sep='\n')

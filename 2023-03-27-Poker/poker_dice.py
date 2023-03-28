from random import randint, seed

FIVE_OF_A_KIND, FOUR_OF_A_KIND, FULL_HOUSE, THREE_OF_A_KIND, \
    TWO_PAIR, ONE_PAIR, BUST, STRAIGHT, BUST_OR_STRAIGHT = 0, 1, 2, 3, 4, 5, 6, 7, 8

catagories = [
    FIVE_OF_A_KIND,
    FOUR_OF_A_KIND,
    FULL_HOUSE,
    THREE_OF_A_KIND,
    TWO_PAIR,
    ONE_PAIR,
    BUST,
    STRAIGHT,
    BUST_OR_STRAIGHT
]
name_catagory = {
    FIVE_OF_A_KIND: "Five of a kind",
    FOUR_OF_A_KIND: "Four of a kind",
    FULL_HOUSE: "Full house",
    THREE_OF_A_KIND: "Three of a kind",
    TWO_PAIR: "Two pair",
    ONE_PAIR: "One pair",
    BUST: "Bust",
    STRAIGHT: "Straight",
    BUST_OR_STRAIGHT: "Bust or straight"
}
name_card = {
    0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Joke', 4: '10', 5: '9'
}
number_card = {
    'Ace': 0, 'King': 1, 'Queen': 2, 'Joke': 3, '10': 4, '9': 5
}


def roll_dice(held=[]):
    roll = [randint(0, 5) for _ in range(5 - len(held))]
    roll.extend(held)
    roll.sort()
    return (0, 1, 2, 4, 4)#tuple(roll)


def catagorize(roll):
    # roll.sort()
    fingerprint = [roll.count(_) for _ in range(6)]
    fingerprint.sort()
    fingerprint = tuple(fingerprint) # type: ignore
    pool = {
        (0, 0, 0, 0, 0, 5): FIVE_OF_A_KIND,
        (0, 0, 0, 0, 1, 4): FOUR_OF_A_KIND,
        (0, 0, 0, 0, 2, 3): FULL_HOUSE,
        (0, 0, 0, 1, 1, 3): THREE_OF_A_KIND,
        (0, 0, 0, 1, 2, 2): TWO_PAIR,
        (0, 0, 1, 1, 1, 2): ONE_PAIR,
        (0, 1, 1, 1, 1, 1): BUST_OR_STRAIGHT
    }
    busts = set([
        (0, 2, 3, 4, 5),
        (0, 1, 3, 4, 5),
        (0, 1, 2, 4, 5),
        (0, 1, 2, 3, 5)
    ])
    catagory = pool[fingerprint]
    if catagory == BUST_OR_STRAIGHT:
        catagory = BUST if roll in busts else STRAIGHT
    return catagory


def simulate(times):
    possibilities = {}
    for key in catagories:
        possibilities[key] = 0.
    for _ in range(times):
        possibilities[catagorize(
            roll_dice())] += 1. / times
    print('''
     Five of a kind  : {0:.2%}
     Four of a kind  : {0:.2%}
     Full house      : {0:.2%}
     Three of a kind : {0:.2%}
     Two pair        : {0:.2%}
     One pair        : {0:.2%}
     Bust            : {0:.2%}
     Straight        : {0:.2%}
     '''.format(
        possibilities[FIVE_OF_A_KIND],
        possibilities[FOUR_OF_A_KIND],
        possibilities[FULL_HOUSE],
        possibilities[THREE_OF_A_KIND],
        possibilities[TWO_PAIR],
        possibilities[ONE_PAIR],
        possibilities[BUST],
        possibilities[STRAIGHT]
    ))


def ask_held_cards(roll, turn=2):
    while True:
        try:
            held = []
            tmp = list(roll)
            a = f"Which dice do you want to keep for the {'second' if turn == 2 else 'third'} roll?"
            prompts = input(a).split(' ')
            if "all" in prompts or "All" in prompts:
                return roll
            if prompts == ['']:
                return held
            for card in prompts:
                id = number_card[card]
                if id not in tmp:
                    raise ValueError
                del tmp[tmp.index(id)]
                held.append(id)
            break
        except:
            print("That is not possible, try again!")
    return held


def play(generate_only=False):
    def report_roll(roll):
        print(
            f"The roll is: {' '.join([name_card[i] for i in roll])}")
        print(
            f"It is a {name_catagory[catagorize(roll)]}"
        )
    # turn 1
    roll1 = roll_dice()
    if generate_only:
        return roll1
    report_roll(roll1)
    held1 = ask_held_cards(roll1, 2)
    if len(held1) == 5:
        print("Ok, done.")
        return
    # turn 2
    roll2 = roll_dice(held1)
    report_roll(roll2)
    held2 = ask_held_cards(roll2, 3)
    if len(held2) == 5:
        print("Ok, done.")
        return
    # turn 3
    roll3 = roll_dice(held2)
    report_roll(roll3)

play()
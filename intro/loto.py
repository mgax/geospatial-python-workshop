import random

def play(choice):
    draw = random.sample(range(1, 50), 6)

    win = True
    for number in choice:
        if number not in draw:
            win = False

    if win:
        print "you win!", draw

for c in range(100):
    play([11, 27])

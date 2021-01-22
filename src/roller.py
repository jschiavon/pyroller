import numpy as np
from numpy.random import default_rng

_rng = default_rng()

def roller(dice_size=6, dice_number=1):
    return _rng.integers(1, dice_size, endpoint=True, size=(dice_number,))

def roll_dice(size=6, number=1, modifier=0, reroll=0):
    rolls = roller(size, number)
    if isinstance(reroll, str):
        if reroll == 'lowest':
            idx = np.argmin(rolls)
            rolls[idx] = roller(size)
        elif reroll == '2lowest':
            idx = np.argpartition(rolls, 2)[:2]
            rolls[idx] = roller(size, dice_number=2)
    elif (reroll > 0):
        rolls = np.array([x if x > reroll else roller(size).sum() for x in rolls])
    return rolls.sum() + modifier

def meanroll(size=6, number=1, modifier=0, reroll=0, repeat=1e4):
    repeat = int(repeat)
    res = sum(roll_dice(size, number, modifier, reroll) for _ in range(repeat))
    return res / repeat

def minroll(size=6, number=1, modifier=0):
    return 1 * number + modifier

def maxroll(size=6, number=1, modifier=0):
    return size * number + modifier

def roll_stats(size=6, number=1, modifier=0, reroll=0, statistics='all'):
    if statistics in ['min', 'all']:
        stat = minroll(size, number, modifier)
        if statistics == 'all':
            mi = stat
    if statistics in ['max', 'all']:
        stat = maxroll(size, number, modifier)
        if statistics == 'all':
            ma = stat
    if statistics in ['mean', 'all']:
        stat = meanroll(size, number, modifier, reroll, repeat=1e4)
        if statistics == 'all':
            me = stat
    if statistics == 'all':
        return mi, me, ma
    return stat


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='simple command line utility for dice roller')
    parser.add_argument('-d', '--dice_size', metavar='D', default=6, type=int,
                        help="The number of faces of the dice (default 6)")
    parser.add_argument('-n', '--dice_number', metavar='N', default=1, type=int,
                        help="The number of rolled dices (default 1)")
    parser.add_argument('-m', '--modifier', metavar='M', default=0, type=int,
                        help="A modifier for the roll (default 0)")
    parser.add_argument('-r', '--reroll', metavar='R', default=0, type=int,
                        choices=[0, 1, 2],
                        help="A modifier for the roll (default 0)")
    args = parser.parse_args()
    sz = args.dice_size
    n = args.dice_number
    m = args.modifier
    r = args.reroll

    result = roll_dice(size=sz,
                       number=n,
                       modifier=m,
                       reroll=r)
    mi, me, ma = all_stats(size=sz,
                       number=n,
                       modifier=m,
                       reroll=r)
    print('Result of {0}d{1}{2}{3}: {4}'.format(
        n, sz, f'+{m}' if m > 0 else '', ' with reroll' if r > 0 else '',
        result))
    print('Result in [{} - {}], Mean: {:.2f}'.format(mi, ma, me))

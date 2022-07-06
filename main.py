from itertools import permutations
from math import factorial
from tqdm import tqdm

def rank_score(rankings, distribution):
    score = [0 for _ in range(len(list(rankings.values())[0]))]
    for i in range(len(rankings)):
        try:
            score[rankings[list(rankings.keys())[i]].index(distribution[i])] += 1
        except:
            pass

    return ''.join(map(str, score))

def permutations_count(n, r):
    numer = factorial(n)
    denom = factorial(n-r)
    return numer//denom

def rma(rankings, items, progress_bar=False):
    scores_dict = {}

    if progress_bar == True:
        with tqdm(total=permutations_count(l:=len(items), l)) as pbar:
            for p in permutations(items, l):
                scores_dict[p] = rank_score(rankings, p)
                pbar.update(1)

    if progress_bar == False:
        for p in permutations(items, len(items)):
            scores_dict[p] = rank_score(rankings, p)

    return {s:scores_dict[s] for s in sorted(scores_dict, key=scores_dict.get, reverse=True)}

if __name__ == '__main__':
    from random import sample

    while True:

        progress_bar = input('Progress bar (y/n): ')
        if 'y' in progress_bar.lower():
            progress_bar = True
        else:
            progress_bar = False

        print_all = input('Print all permutations (y/n): ')

        count_items = int(input('Number of items: '))
        count_ranks = int(input('Number of preferences: '))
        print()

        items = [i+1 for i in range(count_items)]

        rankings = {i+1:sample(items, count_ranks) for i in range(count_items)}
        for key in rankings:
            print(key, rankings[key])
        print()

        for key in (sd := rma(rankings, items, progress_bar)):
            if 'y' in print_all.lower():
                print(key, sd[key])
            else:
                pass
        print()

        print('All Rank-Maximal solutions:')
        rank_maximal = list(sd.values())[0]
        for key in sd:
            if sd[key] == rank_maximal:
                print(key, sd[key])
            else:
                break

        print()

        hold = input()

from collections import Counter, defaultdict, deque

lines = [x for x in open('day21/0.in').read().splitlines()]
all_ingrs = set()
candidates = defaultdict(list)  # allergen: candidate ingredients
for line in lines:
    ingr_str, _, alrg_str = line.partition(' (contains ')
    ingrs = ingr_str.split()
    all_ingrs.update(ingrs)
    alrgs = alrg_str.removesuffix(')').split(', ')
    for alrg in alrgs:
        candidates[alrg].append(ingrs)

translated = {}  # allergen: single ingredient
queue = deque(candidates.keys())
while queue:  # Whittle down the candidate allergens list by looking for single ingredients
    alrg = queue.popleft()
    ingr_set = set.intersection(*map(set, candidates[alrg]))
    if len(ingr_set) == 1:  # We've translated an allergen
        translated[alrg] = ingr_set.pop()  # Add it to the decoder ring
        for ingrs in candidates.values():  # And remove it from any other candidates
            for i in ingrs:
                if translated[alrg] in i:
                    i.remove(translated[alrg])
    else:  # Otherwise, re-enqueue it and come back to it later
        queue.append(alrg)

# Solved this backwards - Part 1 is looking for the unknown ingredients
untranslated = all_ingrs - set(translated.values())
word_cnt = dict(Counter(open('day21/0.in').read().split()))
ans1 = sum([v for k, v in word_cnt.items() if k in untranslated])
print(f'Part 1: {ans1}')

ans2 = ','.join(v for _, v in sorted(translated.items()))
print(f'Part 2: {ans2}')

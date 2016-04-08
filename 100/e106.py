import itertools


def create_subsets(full_set):
    subsets = []
    for i in range(1, len(full_set)):
        subsets.append(itertools.combinations(full_set, i))
    subsets = [list(item) for sublist in subsets for item in sublist]
    return subsets


def test_subsets(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    greater = False
    if s1[0] > s2[0]:
        greater = True

    for i in range(0, len(s1)):
        if s1[i] < s2[i] and greater:
            return True
        elif s1[i] > s2[i] and not greater:
            return True
    return False


arr = range(1, 7)

sub_sets = create_subsets(arr)
count = 0
for i in sub_sets:
    for j in sub_sets:
        if i != j and len(i) == len(j) and len(i) > 1 and len(list(set(i) & set(j))) == 0:
            if test_subsets(i, j):
                count += 1

print count / 2

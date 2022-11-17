days = {'Sunday': 0, "Monday":1}
days['Tuesday'] = 2
months = {'Jan' : 0, 'Feb': 1}
dicts = {}
dicts[0] = days
dicts[1] = months
dicts['bananas'] = {0: 'Jaccard',
                   1: 'Jaccard Similarity',
                   2: 'Coffee'}

for k, v in dicts.items():
    print(f'{k}\t{v}')
    for kk, vv in v.items():
        print(f'{k}\t{kk}\t{vv}')



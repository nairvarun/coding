'''
# 1
with open('5.txt') as f:
    seeds, *sections = f.read().split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))
    for section in sections:
        mapping = [list(map(int, i.split())) for i in section.splitlines()[1:]]
        new_seeds = []
        for seed in seeds:
            for dest_start, src_start, range_len in mapping:
                if seed in range(src_start, src_start + range_len):
                    new_seeds.append(seed - src_start + dest_start)
                    break
            else:
                new_seeds.append(seed)
        seeds = new_seeds

    print(min(seeds))
'''

# 2
with open('5.txt') as f:
    seed_range, *sections = f.read().split('\n\n')
    seed_range = list(map(int, seed_range.split(':')[1].split()))
    seeds = [(seed_range[i], seed_range[i] + seed_range[i+1]) for i in range(0, len(seed_range), 2)]

    for section in sections:
        mapping = [list(map(int, i.split())) for i in section.splitlines()[1:]]
        new_seeds = []
        while seeds:
            seed_start, seed_end = seeds.pop()
            for dest_start, src_start, range_len in mapping:
                overlap_start = max(seed_start, src_start)
                overlap_end = min(seed_end, src_start+range_len)

                if overlap_start < overlap_end:
                    new_seeds.append((overlap_start - src_start + dest_start, overlap_end - src_start + dest_start))
                    if overlap_start > seed_start:
                        seeds.append((seed_start, overlap_start))
                    if seed_end > overlap_end:
                        seeds.append((overlap_end, seed_end))
                    break
            else:
                new_seeds.append((seed_start, seed_end))
        seeds = new_seeds

    print(min(seeds)[0])

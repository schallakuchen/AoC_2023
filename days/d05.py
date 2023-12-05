import time

def d05():
    # Read raw text file
    lines = open(f"inputs\\d05.txt").read()

    # Parse input
    input_maps = lines.split("\n\n")
    seeds = [int(seed) for seed in input_maps.pop(0).split(':')[1].strip().split(' ')]
    print(seeds)

    # Split the seeds into pairs to get the ranges for Part 2
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    integer_maps = []

    for maps in input_maps:
        split_maps = maps.split(':\n')[1].split('\n')
        integer_maps.append([list(map(int, item.split())) for item in split_maps])
    print(integer_maps)

    for s_idx, seed in enumerate(seeds):
        print(f"Seed No. {s_idx}")
        for cat_idx, category in enumerate(integer_maps):
            print(f"Category No. {cat_idx}: {category}")
            for m_idx, m in enumerate(category):
                print(f"Map No. {m_idx}: {m}")
                if m[1] <= seed < (m[1] + m[2]):
                    print("yes")
                    seed = m[0] + (seed - m[1])
                    break
                else:
                    print("no")
            print(seed)
            print('\n')
        seeds[s_idx] = seed  # update the seed number for next category
    print(seeds)
    print(f"Part1: {min(seeds)}")

    # Part 2
    seeds_part2 = []
    # Alter zu fette Liste xDD
    '''
    for seed_range in seed_ranges:
        print(seed_range)
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            seeds_part2.append(seed)
    print(seeds_part2)
    '''

    # Just iterate in the range instead of creating the bf list
    lowest_location_number = float('inf')
    print(f"Lowest number before: {lowest_location_number}")
    print("Part 2 is processing. Wish me luck...")
    start_time = time.time()
    print(start_time)
    for seed_range in seed_ranges:
        for s_index, seed in enumerate(range(seed_range[0], seed_range[0] + seed_range[1] - 1)):
            # print(f"Seed No. {s_idx}")
            temp_seed = seed
            for cat_idx, category in enumerate(integer_maps):
                # print(f"Category No. {cat_idx}: {category}")
                for m_idx, m in enumerate(category):
                    # print(f"Map No. {m_idx}: {m}")
                    if m[1] <= seed < (m[1] + m[2]):
                        # print("yes")
                        temp_seed = m[0] + (seed - m[1])
            if temp_seed < lowest_location_number:
                lowest_location_number = temp_seed
    print(seeds_part2)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time it took for the lazy approach: {elapsed_time}")
    print(f"Part2: {lowest_location_number}")


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()

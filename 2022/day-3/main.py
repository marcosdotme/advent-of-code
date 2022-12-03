# PART 1

from string import ascii_letters

priority = {
    ascii_letters[i]: i + 1 for i in range(len(ascii_letters))
}

sum_priorities = 0

with open('input.txt') as file:
    rucksacks = file.read().split('\n')

    for rucksack in rucksacks:
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]

        common_item_types = ''.join(set(first_half).intersection(second_half))
        sum_priorities += priority[common_item_types]

    print(sum_priorities)


# PART 2

sum_priorities = 0

with open('input.txt') as file:
    rucksacks = file.read().split('\n')

    for i in range(0, len(rucksacks), 3):
        group = [
            rucksacks[i],
            rucksacks[i + 1],
            rucksacks[i + 2]
        ]

        rucksack_badge = ''.join(set.intersection(*map(set, group)))
        sum_priorities += priority[rucksack_badge]

    print(sum_priorities)

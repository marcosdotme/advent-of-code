# PART 1

elf_calorie_sum = 0
elf_max_calorie = 0

with open('input.txt') as file:
    data = (
        [
            list(map(int, elf.splitlines())) for elf in file.read().split('\n\n')
        ]
    )

    for elf in data:
        elf_calorie_sum = sum(elf)

        if elf_calorie_sum > elf_max_calorie:
            elf_max_calorie = elf_calorie_sum
    
    print(elf_max_calorie)


# PART 2

elf_total_calories_carrying = list()

with open('input.txt') as file:
    data = (
        [
            list(map(int, elf.splitlines())) for elf in file.read().split('\n\n')
        ]
    )

    for elf in data:
        elf_calorie_sum = sum(elf)

        elf_total_calories_carrying.append(elf_calorie_sum)

elf_total_calories_carrying = sorted(elf_total_calories_carrying)
top_3_elf = elf_total_calories_carrying[-3:]

print(sum(top_3_elf))

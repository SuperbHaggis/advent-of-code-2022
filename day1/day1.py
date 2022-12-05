raw_data = open('data.txt', 'r').read()
split_data = [entry.split('\n') for entry in raw_data.split('\n\n')]

def get_calories_per_elf(data):
    calories_per_elf = []
    for elf in data:
        calories = []
        for snack in elf:
            calories.append(int(snack))
        calories_per_elf.append(sum(calories))
    return calories_per_elf

calories_per_elf = get_calories_per_elf(split_data)
highest_calories = max(get_calories_per_elf(split_data))
calories_per_elf.sort(reverse=True)
top_three_calories = sum(calories_per_elf[0:3])

print(highest_calories)
print(top_three_calories)

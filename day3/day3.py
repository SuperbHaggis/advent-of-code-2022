raw_data = open('data.txt', 'r').read().split('\n')

def get_rucksacks():
	rucksacks = []
	for rucksack in raw_data:
		first_compartment = rucksack[:len(rucksack)//2]
		second_compartment = rucksack[len(rucksack)//2:]
		rucksacks.append([first_compartment, second_compartment])
	return rucksacks

def get_shared_items(rucksacks):
	shared_items = []
	for rucksack in rucksacks:
		shared_items.append((set(rucksack[0]) & set(rucksack[1])).pop())
	return shared_items

def get_letter_values(shared_items):
	letter_values = []
	for item in shared_items:
		ascii_value = ord(item)
		if ascii_value < 97:
			letter_values.append(ascii_value - 38)
		else:
			letter_values.append(ascii_value - 96)
	return letter_values

def get_groups(rucksacks):
	groups = []
	rucksack_index = 0
	while rucksack_index < len(rucksacks):
		groups.append([rucksacks[rucksack_index], rucksacks[rucksack_index + 1], rucksacks[rucksack_index + 2]])
		rucksack_index += 3
	return groups

def get_group_badges(groups):
	badges = []
	for group in groups:
		badges.append((set(group[0]) & set(group[1]) & set(group[2])).pop())
	return badges


rucksacks = get_rucksacks()
shared_items = get_shared_items(rucksacks)
shared_items_values = get_letter_values(shared_items)
groups = get_groups(raw_data)
badge_values = get_letter_values(get_group_badges(groups))

print('Sum of Shared Items: %s' % sum(shared_items_values))
print('Sum of Badges: %s' % sum(badge_values))
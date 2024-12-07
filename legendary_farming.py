# using dictionaries and dictionary comprehension:
# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# Input
# •	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Output
# •	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# •	On the next three lines, print the remaining key materials
# •	On the several final lines, print the junk items
# •	All materials should be printed in the format: "{material}: {quantity}"
# •	The output should be lowercase, except for the first letter of the legendary


key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
legendary_items = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}
obtained = False

while not obtained:
    materials = input().lower().split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                print(f"{legendary_items[material]} obtained!")
                obtained = True
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = 0
            junk_materials[material] += quantity


print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")


for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")

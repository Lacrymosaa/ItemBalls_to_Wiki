import re
from collections import defaultdict

with open('ItemBalls.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()

items_map = defaultdict(list)

map_regex = re.compile(r"Map ID: \d+\. (.+)")
item_regex = re.compile(r"item: ([A-Z,\d]+)")

current_map = None

for line in file_content.splitlines():
    map_match = map_regex.search(line)
    if map_match:
        current_map = map_match.group(1)

    item_match = item_regex.search(line)
    if item_match and current_map:
        item = item_match.group(1).strip()
        items_map[item].append(current_map)

output_lines = []
for item, maps in items_map.items():
    line = f"{item}, Maps: {', '.join(maps)}"
    output_lines.append(line)

output_path = 'output_items.txt'
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(output_lines))

print(f"Output salvo em {output_path}")


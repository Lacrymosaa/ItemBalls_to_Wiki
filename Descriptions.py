import re

items_data = {}
with open("items.txt", "r") as f:
    item_block = None
    for line in f:
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            item_block = line[1:-1] 
            items_data[item_block] = {}
        elif "=" in line and item_block:
            key, value = map(str.strip, line.split("=", 1))
            items_data[item_block][key] = value

def update_wiki_table(wiki_content, items_data):
    def replace_row(match):
        item_key = match.group(1).split(".")[0] 
        original_name = match.group(2)
        original_description = match.group(3) 
        location = match.group(4) 
        
        if item_key in items_data:
            name = items_data[item_key].get("Name", original_name)
            description = items_data[item_key].get("Description", original_description)
        else:
            name = original_name
            description = original_description

        return f"| [[File:{item_key}.png|50px]] {name} || {description} || {location}"

    pattern = re.compile(r"\| \[\[File:(.*?)\|50px\]\] (.*?) \|\| (.*?) \|\| (.*?)")
    return re.sub(pattern, replace_row, wiki_content)

with open("wiki.txt", "r") as wiki_file:
    wiki_content = wiki_file.read()

updated_wiki_content = update_wiki_table(wiki_content, items_data)

with open("wiki.txt", "w") as wiki_file:
    wiki_file.write(updated_wiki_content)

print("Tabela da wiki atualizada com sucesso!")

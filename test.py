def convert_clothes_data(clothes_data):
    converted_clothes = {}

    for cloth in clothes_data:
        item_name = cloth['item']
        item_label = cloth['label']

        converted_clothes[item_name] = {
            "['name']": f"'{item_name}'",
            "['label']": f"'{item_label}'",
            "['weight']": 500,
            "['type']": "'item'",
            "['image']": f"'{item_name}.png'",  # Assuming PNG files are named accordingly
            "['unique']": False,
            "['useable']": True,
            "['shouldClose']": True,
            "['combinable']": "nil",
            "['description']": "'Kleider zum anziehen.'"
        }

        if 'equip' in cloth and 'unEquip' in cloth:
            # Add the equip and unEquip data if it's a shirt or jacket
            converted_clothes[item_name]["['--{{']"] = {
                "['arms']": {
                    "['equip']": cloth['equip'],
                    "['unEquip']": cloth['unEquip']
                }
            }

    return converted_clothes

# Sample clothes data (replace this with your actual data)
sample_clothes_data = [
    {
        'item': 'black_helmet',
        'label': 'Black Helmet',
        'values': {
            'id': 53,
            'color': 0,
        },
        'equip': 15,
        'unEquip': 1,
    },
    # Add more items as needed
]

# Convert the sample clothes data
converted_data = convert_clothes_data(sample_clothes_data)

# Print or use converted_data as needed
for item_name, item_data in converted_data.items():
    print(f"[{item_name}] = {",\n".join([f'{k} = {v}' for k, v in item_data.items()])},\n")

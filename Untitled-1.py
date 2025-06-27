from pprint import pprint

# Задача №1:

def read_cook_book(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                })
            cook_book[dish_name] = ingredients
            file.readline()  # читаем пустую строку между рецептами
    return cook_book

cook_book = read_cook_book('recipes.txt')
pprint(cook_book)

# Задача №2:

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюдо "{dish}" отсутствует в кулинарной книге')
            continue
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return shop_list

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_book))

# Задача №3:

def merge_files(files, output_filename):
    file_info = []
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_info.append({
                'name': filename,
                'line_count': len(lines),
                'content': ''.join(lines)
            })
    
    file_info.sort(key=lambda x: x['line_count'])
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        for info in file_info:
            f.write(f"{info['name']}\n{info['line_count']}\n{info['content']}\n")

files_to_merge = ['1.txt', '2.txt', '3.txt']
merge_files(files_to_merge, 'result.txt')

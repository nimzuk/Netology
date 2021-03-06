def make_cook_book_from_file():
    cook_book = {}
    with open('cookbook.txt') as cookbook_file:
        # cookbook_file.readline()
        for line in cookbook_file:
            dish_name = cookbook_file.readline().lower()
            # print(dish_name)
            # ing_amount = cookbook_file.readline()
            ing_amount = int(cookbook_file.readline())
            # print(ing_amount)
            ingredients = []
            for i in range(1, ing_amount):
                ingredient = {}
                part = cookbook_file.readline().lower().strip().split(' | ')
                ingredient['ingridient_name'] = part[0]
                ingredient['quantity'] = int(part[1])
                ingredient['measure'] = part[2]
                ingredients.append(ingredient)
            cook_book[dish_name.strip()] = ingredients
            cookbook_file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

cook_book = make_cook_book_from_file()
create_shop_list()
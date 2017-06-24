def groupingDishes(dishes):
    ingredients={}
    for dish in dishes:
        this_dish=dish[0]
        this_ingredients=dish[1:]
        for ingredient in this_ingredients:
            if not ingredient in ingredients:
                ingredients[ingredient]=set()
            ingredients[ingredient].add(this_dish)
    groupedDishes=[]
    for ingredient in ingredients:
        if len(ingredients[ingredient])>=2:
            this_list=[ingredient]
            this_list.extend(sorted(list(ingredients[ingredient])))
            groupedDishes.append(this_list)
    return sorted(groupedDishes)

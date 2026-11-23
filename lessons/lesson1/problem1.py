def hero_name(color, animal, superpower="невидимость", name= "Капитан"):
    return f"{name} {color.lower()} {animal.lower()} ({superpower})"

print(hero_name("Синий", "Енот"))
print(hero_name("Красный", "Дельфин", "левитация", "Генерал"))
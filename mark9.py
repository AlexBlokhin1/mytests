# list_rabbit = 'Айдахский кролик, или кролик-пигмей hjkhj — млекопитающее семейства зайцевых. Длина тела составляет от 22 до 28 см, вес от 250 до 450 г. Окрас шерсти верхней части тела жёлто-коричневого цвета, нижняя часть тела белёсая. Задние конечности очень короткие, поэтому у них отсутствует прыгающий способ передвижения как у других зайцев. Размножается в Америке.'
# alphabet ='abcdefghijklmnopqrstuvwxyz'
#
#
# def check_characters():
#     for letter in list_rabbit:
#         for char in alphabet:
#             if char == letter:
#                 return ('YOU CANT POST THIS TEXT')
#     return "OK"
#
# b = check_characters()
# print(b)

BIG_TEXT = """
Paxillus involutus, the common roll-rim, is a fungus widely distributed across the Northern Hemisphere; it has also been unintentionally introduced to Australia, New Zealand, and South America. The brownish fruit body grows up to 6 cm (2.4 in) high. It has a funnel-shaped cap up to 12 cm (5 in) wide with a distinctive in-rolled rim and decurrent gills close to the stalk. Genetic testing suggests that the fungus may be a species complex rather than a single species. A common mushroom of deciduous and coniferous woods and grassy areas in late summer and autumn, P. involutus is symbiotic with the roots of many tree species, reducing the trees' intake of heavy metals and increasing their resistance to pathogens. Previously considered edible and eaten widely in Eastern and Central Europe, the mushroom has been found to be dangerously poisonous; in 1944, it killed the German mycologist Julius Schäffer. It can trigger the immune system to attack red blood cells with potentially fatal complications, including acute renal and respiratory failure. (Full article...)
"""
ban_words = ['gghfg']


import re

a = (re.findall(r"[\w']+", BIG_TEXT))


def chexk_func():
    for word in a:
        for ban_word in ban_words:
            if word == ban_word:
                return 'You cant post this text'
    return 'OK'


p = chexk_func()
print(p)
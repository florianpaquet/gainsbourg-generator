#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import choice


start_words = [
    u"Si j'ai quoi",
    u"Si je baise",
    u"Des salopes",
    u"Des gamines",
    u"Si je bande",
    u"Pour des putes",
    u"Brunes blondes",
    u"Si j'assure",
    u"D'la technique",
    u"Self control",
    u"Si j'aime ça",
    u"Peut importe",
    u"Obsédé",
    u"Peut importe",
]

middle_words = [
    u"affirmatif",
    u"et quoi d'autre",
    u"quoi des noms",
    u"des actrices",
    u"de quel âge",
    u"pour qui ça",
    u"et qui d'autre",
    u"et rouquines",
    u"quoi tout seul",
    u"du doigté",
    u"comment ça",
    u"quel côté",
    u"c'que j'préfère",
    u"sexuel",
]

end_words = [
    u"no comment",
    u"ooh ooh ooh",
]


for i in range(20):
    print(u"%s %s %s %s" % (choice(start_words), choice(middle_words), choice(middle_words), choice(end_words)))

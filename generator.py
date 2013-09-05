#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import shuffle, choice


class GainsbourgGenerator(object):
    """
    Random Gainsbourg lyrics generator
    """
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

    def __init__(self):
        self.tmp_middle_words = None

    def _copy_middle_words(self):
        """
        Stores a copy of middle words if necessary
        """
        if self.tmp_middle_words is None:
            self.tmp_middle_words = list(self.middle_words)

    def _random_middle_word(self):
        """
        Returns random middle word
        """
        self._copy_middle_words()
        shuffle(self.tmp_middle_words)
        return self.tmp_middle_words.pop()

    def random_sentence(self, last=False):
        """
        Returns a random sentence
        """
        sentence = u"{start_word}{comma} {first_middle_word} {second_middle_word} {end_word}".format(
            start_word=choice(self.start_words),
            comma=',' if not last else '',
            first_middle_word=self._random_middle_word(),
            second_middle_word=self._random_middle_word(),
            end_word="ooh ooh ooh" if last else "no comment"
        )
        self.tmp_middle_words = None
        return sentence

    def random_verse(self):
        """
        Returns a random verse as a list of 4 sentences
        """
        return [self.random_sentence(i==3) for i in range(4)]


if __name__ == '__main__':
    generator = GainsbourgGenerator()
    for i in range(5):
        print('%s\n' % '\n'.join(generator.random_verse()))

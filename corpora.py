import os
import random


class Names(object):
    """A class that accesses names corpora to return random names."""
    masculine_forenames = tuple(
        name[:-1] for name in
        open(os.getcwd()+'/corpora/masculine_names.txt', 'r')
    )
    feminine_forenames = tuple(
        name[:-1] for name in
        open(os.getcwd()+'/corpora/feminine_names.txt', 'r')
    )
    english_surnames = tuple(
        name.strip('\n') for name in
        open(os.getcwd()+'/corpora/english_surnames.txt', 'r')
    )
    french_surnames = tuple(
        name.strip('\n') for name in
        open(os.getcwd()+'/corpora/french_surnames.txt', 'r')
    )
    german_surnames = tuple(
        name.strip('\n') for name in
        open(os.getcwd()+'/corpora/german_surnames.txt', 'r')
    )
    irish_surnames = tuple(
        name.strip('\n') for name in
        open(os.getcwd()+'/corpora/irish_surnames.txt', 'r')
    )
    scandinavian_surnames = tuple(
        name.strip('\n') for name in
        open(os.getcwd()+'/corpora/scandinavian_surnames.txt', 'r')
    )
    all_surnames = (
        english_surnames + french_surnames + irish_surnames +
        scandinavian_surnames
    )

    @classmethod
    def a_masculine_name(cls):
        """Return a random masculine first name."""
        return random.choice(cls.masculine_forenames)

    @classmethod
    def a_feminine_name(cls):
        """Return a random feminine first name."""
        return random.choice(cls.feminine_forenames)

    @classmethod
    def an_english_surname(cls):
        """Return a random English surname."""
        return random.choice(cls.english_surnames)

    @classmethod
    def a_french_surname(cls):
        """Return a random French surname."""
        return random.choice(cls.french_surnames)

    @classmethod
    def a_german_surname(cls):
        """Return a random German surname."""
        return random.choice(cls.german_surnames)

    @classmethod
    def an_irish_surname(cls):
        """Return a random Irish surname."""
        return random.choice(cls.irish_surnames)

    @classmethod
    def a_scandinavian_surname(cls):
        """Return a random Scandinavian surname."""
        return random.choice(cls.scandinavian_surnames)

    @classmethod
    def any_surname(cls):
        """Return a random surname of any ethnicity."""
        return random.choice(cls.all_surnames)
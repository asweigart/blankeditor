
ENGLISHMAN, SPANIARD, UKRAINIAN, NORWEGIAN, JAPANESE = ('Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese')
ALL_NATIONALITIES = [ENGLISHMAN, SPANIARD, UKRAINIAN, NORWEGIAN, JAPANESE]

COFFEE, WATER, TEA, MILK, ORANGE_JUICE = ('coffee', 'water', 'tea', 'milk', 'orange juice')
ALL_DRINKS = [COFFEE, WATER, TEA, MILK, ORANGE_JUICE]

OLD_GOLD, KOOLS, LUCKY_STRIKE, PARLIAMENTS, CHESTERFIELDS = ('Old Gold', 'Kools', 'Lucky Strike', 'Parliaments', 'Chesterfields')
ALL_SMOKES = [OLD_GOLD, KOOLS, LUCKY_STRIKE, PARLIAMENTS, CHESTERFIELDS]

GREEN, IVORY, YELLOW, BLUE, RED = ('green', 'ivory', 'yellow', 'blue', 'red')
ALL_COLORS = [GREEN, IVORY, YELLOW, BLUE, RED]

DOG, SNAILS, FOX, HORSE, ZEBRA = ('dog', 'snails', 'fox', 'horse', 'zebra')
ALL_PETS = [DOG, SNAILS, FOX, HORSE, ZEBRA]

import itertools, logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(level=logging.CRITICAL)

def solution():
    solutionsSkipped = 0 
    # nationality
    for nationalities in itertools.permutations(ALL_NATIONALITIES, 5):
        # Rule 10
        if nationalities[0] != NORWEGIAN:
            solutionsSkipped += 120**4
            continue
        for colors in itertools.permutations(ALL_COLORS, 5):
            # Rule 2
            if nationalities.index(ENGLISHMAN) != colors.index(RED):
                solutionsSkipped += 120**3
                continue
            # Rule 6
            if colors.index(IVORY) + 1 != colors.index(GREEN):
                solutionsSkipped += 120**3
                continue
            # Rule 15
            if nationalities.index(NORWEGIAN) not in (colors.index(BLUE) - 1, colors.index(BLUE) + 1):
                solutionsSkipped += 120**3
                continue

            for pets in itertools.permutations(ALL_PETS, 5):
                # Rule 3
                if nationalities.index(SPANIARD) != pets.index(DOG):
                    solutionsSkipped += 120**2
                    continue

                for drinks in itertools.permutations(ALL_DRINKS, 5):
                    # Rule 4
                    if colors.index(GREEN) != drinks.index(COFFEE):
                        solutionsSkipped += 120
                        continue
                    # Rule 5
                    if nationalities.index(UKRAINIAN) != drinks.index(TEA):
                        solutionsSkipped += 120
                        continue
                    # Rule 9
                    if drinks[2] != MILK:
                        solutionsSkipped += 120
                        continue


                    for smokes in itertools.permutations(ALL_SMOKES, 5):
                        # Rule 7
                        if smokes.index(OLD_GOLD) != pets.index(SNAILS):
                            continue
                        # Rule 8
                        if smokes.index(KOOLS) != colors.index(YELLOW):
                            continue
                        # Rule 11
                        if smokes.index(CHESTERFIELDS) not in (pets.index(FOX) - 1, pets.index(FOX) + 1):
                            continue
                        # Rule 12
                        if smokes.index(KOOLS) not in (pets.index(HORSE) - 1, pets.index(HORSE) + 1):
                            continue
                        # Rule 13
                        if smokes.index(LUCKY_STRIKE) != drinks.index(ORANGE_JUICE):
                            continue
                        # Rule 14
                        if smokes.index(PARLIAMENTS) != nationalities.index(JAPANESE):
                            continue

                        logging.debug('Skipped: %s' % (solutionsSkipped))
                        logging.debug('Nationalities: %s' % (nationalities,))
                        logging.debug('Colors:        %s' % (colors,))
                        logging.debug('Pets:          %s' % (pets,))
                        logging.debug('Drinks:        %s' % (drinks,))
                        logging.debug('Smokes:        %s' % (smokes,))

                        return 'It is the %s who drinks the water.\nThe %s keeps the zebra.' % (nationalities[drinks.index(WATER)], nationalities[pets.index(ZEBRA)])



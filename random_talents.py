from talents import TALENTS
from random import choice, randint


def unpack_tree(to_unpack, tree):
    unpacked_tree = {key: value for (key, value) in to_unpack.items() if value['tree'] == tree}
    return unpacked_tree


def unpack_cost(to_unpack, cost):
    unpacked_cost = {key: value for (key, value) in to_unpack.items() if value['cost'] == cost}
    return unpacked_cost


mind_talents = unpack_tree(TALENTS, 'mind')
body_talents = unpack_tree(TALENTS, 'body')
spirit_talents = unpack_tree(TALENTS, 'spirit')


def roll_talents():
    MAX_SPEND = 7

    first_roll = randint(1, 4)
    second_roll = randint(1, 4)

    remaining_spend = MAX_SPEND - (first_roll + second_roll)

    if remaining_spend >= 4:
        third_roll = randint(1, 4)

    else:
        third_roll = randint(0, remaining_spend)

    if first_roll == 0:
        mind_talent = "None"
    else:
        mind_talent = choice(list(unpack_cost(mind_talents, first_roll)))

    if second_roll == 0:
        body_talent = "None"
    else:
        body_talent = choice(list(unpack_cost(body_talents, second_roll)))

    if third_roll == 0:
        spirit_talent = "None"
    else:
        spirit_talent = choice(list(unpack_cost(spirit_talents, third_roll)))
    return (f"***Talents***\nMind: {mind_talent}\nBody: {body_talent}\nSpirit: {spirit_talent}\n")

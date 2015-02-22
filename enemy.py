# This script is written for the sole purpose of producing enemy cards for project Hammond

import random as r

BODY_PARTS = ["head", "torso", "left arm", "right arm", "left leg", "right leg"]
BLOCK_ZONES = ["upper", "central", "lower"]

def gen_numbers(max_hits, max_blocks, level):
    hit_list = []
    block_list = []

    for hit in range(max_hits):
        if (level/10 * 35) + 65 > r.randint(1,100):
            hit_list += [r.randint(0, 5)]

    for block in range(max_blocks):
        if (level/10 * 25) + 25 > r.randint(1,100):
            block_list += [r.randint(0, 2)]

    return (hit_list, block_list)

def pretty_print(hit_list, block_list):
    for hit in hit_list:
        print "They strike you in the " + BODY_PARTS[hit] + "!"

    for block in block_list:
        print "They defend themselves in the " + BLOCK_ZONES[block] + " zone."

def print_party_attacks(enemy_num, max_hits, max_blocks, level):
    for i in range(enemy_num):
        this_enemy = gen_numbers(max_hits, max_blocks, level)
        print "Enemy " + str(i + 1) + " attacks with:"
        pretty_print(this_enemy[0], this_enemy[1])
        print ""

from game_params import *

raw_data = open('data.txt', 'r').read()
game_pairs = [pair.split() for pair in raw_data.split('\n')]

def get_score_pt1():
    total_score = 0
    for pair in game_pairs:
        round_score = 0
        if winning_pairs.__contains__(pair):
            round_score = 6 + shape_scores[pair[1]]
        elif draw_pairs.__contains__(pair):
            round_score = 3 + shape_scores[pair[1]]
        else:
            round_score = shape_scores[pair[1]]
        total_score += round_score
    return total_score

def get_score_pt2():
    total_score = 0
    for pair in game_pairs:
        round_score = 0
        if pair[1] == 'X':
            round_score = shapes[shapes[pair[0]]['win']]['score']
        elif pair[1] == 'Y':
            round_score = 3 + shapes[shapes[pair[0]]['draw']]['score']
        else:
            round_score = 6 + shapes[shapes[pair[0]]['lose']]['score']
        total_score += round_score
    return total_score

print('Part 1 Score: %s' % get_score_pt1())
print('Part 2 Score: %s' % get_score_pt2())
winning_pairs = [
    ['A', 'Y'],
    ['B', 'Z'],
    ['C', 'X']
]

draw_pairs = [
    ['A', 'X'],
    ['B', 'Y'],
    ['C', 'Z']
]

shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

shapes = {
    'A': {
        'win': 'C',
        'draw': 'A',
        'lose': 'B',
        'score': 1
    },
    'B': {
        'win': 'A',
        'draw': 'B',
        'lose': 'C',
        'score': 2
    },
    'C': {
        'win': 'B',
        'draw': 'C',
        'lose': 'A',
        'score': 3
    }
}

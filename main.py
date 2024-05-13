import sys
import time
from itertools import cycle

PAUSE = 0.3

ROWS = [
    '        #--#',
    '       #{}--{}#',
    '      #{}-----{}#',
    '     #{}-------{}#',
    '    #{}--------{}#',
    '    #{}-------{}#',
    '     #{}-----{}#',
    '      #{}---{}#',
    '       #{}-{}#',
]

nucleotide_pairs = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]
nucleotide_pairs_cycle = cycle(nucleotide_pairs)

try:
    print('DNA Visualizer')
    print('Press Ctrl-C to quit...')
    time.sleep(1)

    rowIndex = 0
    while True:
        rowIndex = (rowIndex + 1) % len(ROWS)

        if rowIndex == 0 or rowIndex == len(ROWS) - 1:
            print(ROWS[rowIndex])
            continue

        row = ROWS[rowIndex].format(next(nucleotide_pairs_cycle)[0], next(nucleotide_pairs_cycle)[1])
        print(row)
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()
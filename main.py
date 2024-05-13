import time
from itertools import cycle
from typing import List, Tuple

# Constants
PAUSE = 0.3
NUCLEOTIDE_PAIRS = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]


# Helper functions
def print_with_spacing(rows: List[str], spacing: int = 8) -> None:
    """Print each row with a specified spacing."""
    for row in rows:
        print(' ' * spacing + row)


def create_row(row_template: str, pair: Tuple[str, str]) -> str:
    """Create a row by formatting the row template with the given nucleotide pair."""
    return row_template.format(*pair)


def main() -> None:
    """Run the DNA Visualizer animation."""
    print('DNA Visualizer')
    print('Press Ctrl-C to quit...')
    time.sleep(1)

    rows = [
        '        #--#',
        '       #{}--{}#',
        '      #{}-----{}#',
        '     #{}-------{}#',
        '    #{}--------{}#',
        '    #{}-------{}#',
        '     #{}-----{}#',
        '      #{}---{}#',
        '       #--#',
    ]

    nucleotide_pairs_cycle = cycle(NUCLEOTIDE_PAIRS)

    row_index = 0
    try:
        while True:
            row_index = (row_index + 1) % len(rows)

            if row_index == 0 or row_index == len(rows) - 1:
                print_with_spacing([rows[row_index]])
            else:
                pair = next(nucleotide_pairs_cycle)
                print_with_spacing([create_row(rows[row_index], pair)])

            time.sleep(PAUSE)
    except KeyboardInterrupt:
        pass  # Clean exit


if __name__ == '__main__':
    main()

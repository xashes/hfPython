"""Module docstring"""
MOVIES = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, [
        "Graham Chapman", [
            "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idel",
            "Terry Jones"
        ]
    ]
]

import sys

def lol_print(lol, indent=False, level=0, output=sys.stdout):
    """Function docstring"""
    for item in lol:
        if isinstance(item, list):
            lol_print(item, indent, level+1, output)
        else:
            if indent:
                print("\t"*level, end='', file=output)
            print(item, file=output)


if __name__ == '__main__':
    lol_print(MOVIES, 1)

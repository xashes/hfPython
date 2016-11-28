"""Module docstring"""
MOVIES = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, [
        "Graham Chapman", [
            "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idel",
            "Terry Jones"
        ]
    ]
]

def lol_print(lol):
    """Function docstring"""
    for item in lol:
        if isinstance(item, list):
            lol_print(item)
        else:
            print(item)

if __name__ == '__main__':
    lol_print(MOVIES)

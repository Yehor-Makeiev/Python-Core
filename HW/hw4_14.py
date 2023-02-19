import sys
from pathlib import Path
print(sys.argv)


try:
    path = Path(sys.argv[1])
    print(path.exists())
except IndexError as e:
    print(f"Sorry, No parameter")


def parse_args():
    result = ""
    for arg in sys.argv:
        return ' '.join(sys.argv[1:])

    return result

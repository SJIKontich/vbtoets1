from lib.utils import *

try:
    import vraag02
    from vraag02 import C
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag02_case1():
    check_exact_match(vraag02, "C", (0, 0), 1)

def test_vraag02_case2():
    check_exact_match(vraag02, "C", (1, 0), 1)
    check_exact_match(vraag02, "C", (2, 0), 1)
    check_exact_match(vraag02, "C", (3, 0), 1)

def test_vraag02_case3():
    check_exact_match(vraag02, "C", (1, 1), 1)
    check_exact_match(vraag02, "C", (2, 1), 2)
    check_exact_match(vraag02, "C", (2, 2), 1)
    check_exact_match(vraag02, "C", (3, 1), 3)
    check_exact_match(vraag02, "C", (3, 2), 3)
    check_exact_match(vraag02, "C", (3, 3), 1)

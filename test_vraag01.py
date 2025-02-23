from lib.utils import *

try:
    import vraag01
    from vraag01 import naar_links1
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag01_case1():
    check_exact_match(vraag01, "naar_links1", ([8, 2, 2, 0], 0), [8, 2, 2, 0])

def test_vraag01_case2():
    check_exact_match(vraag01, "naar_links1", ([8, 2, 2, 0], 3), [8, 2, 2, 0])

def test_vraag01_case3():
    check_exact_match(vraag01, "naar_links1", ([8, 2, 2, 0], 2), [8, 4, 0, 0])

def test_vraag01_case4():
    check_exact_match(vraag01, "naar_links1", ([8, 0, 2, 0], 2), [8, 2, 0, 0])

def test_vraag01_case5():
    check_exact_match(vraag01, "naar_links1", ([8, 2, 2, 0], 1), [8, 2, 2, 0])

from lib.utils import *

try:
    import vraag04
    from vraag04 import integraal
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def f(x):
    return x ** 2

def test_vraag04():
    check_exact_match(vraag04, "integraal", (f, 0, 1, 100), 0.33332500000000037)

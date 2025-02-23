from lib.utils import *

try:
    import vraag05
    from vraag05 import variantie
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag05():
    check_approx_match(vraag05, "variantie", ([1, 2, 3],[0.2, 0.5, 0.3],2.1), 0.49)

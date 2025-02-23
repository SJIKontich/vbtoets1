# Volgende functie zet een lijst om in een gecomprimeerde (kortere) lijst
# De manier waarop is niet belangrijk en de functie werkt correct.

# Onderaan staat een voorbeeld van de output.
# a) Schrijf een test die de functie middle_out test.
# b) Gebruik de debugger om te achterhalen wat de waarde van i is na de while loop.

def middle_out(lst):
    n = len(lst)
    if n <= 2:
        return lst

    result = lst[:1]  # Start with the first element
    i = 1
    while i < n - 1:
        window_size = min(i + 1, n - i - 1)
        window = lst[i:i + window_size]
        avg = sum(window) / len(window)
        result.append(avg)
        i += window_size

    result.append(lst[-1])  # End with the last element
    return result

print(middle_out([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# a) Schrijf een test die de functie middle_out test.
def test_middle_out():
    assert middle_out([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2.5, 5.5, 8.5, 10]

# b) Gebruik de debugger om te achterhalen wat de waarde van i is na de while loop.
# Zet een breakpoint op regel 22 en lees de waarde van i gewoon af: i = 9
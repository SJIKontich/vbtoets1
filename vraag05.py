
# Variantie

# Bereken de variantie van een frequentietabel.
# De waarden zijn gegeven in de lijst waarden en de relatieve frequenties in de lijst frequenties.
# Het gemiddelde van de waarden is gegeven in de parameter gemiddelde.

# Formule:
# variantie = som((waarde - gemiddelde)^2 * frequentie) voor alle waarden

# Voorbeeld:
# >>> variantie([1, 2, 3], [0.2, 0.5, 0.3], 2.1)
# 0.49

def variantie(waarden, frequenties, gemiddelde):
    som = 0
    for i in range(len(waarden)):
        som = som + (waarden[i] - gemiddelde) ** 2 * frequenties[i]
    return som
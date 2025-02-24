
# Integraal

# Hieronder staat de code om de integraal te berekenen van `f` tussen `a` en `b` met 'n' deelintervallen.
# De functie gebruikt telkens de linker grens van het deelinterval om de waarde van `f` te berekenen.
# Pas de code aan zodat die het midden gebruikt.

def f(x):
    return x**2

def integraal(f, a, b, n):
    # maak variabelen aan voor de som en de breedte van de deelintervallen
    som = 0
    dx = (b - a) / n
    # x neemt de eerste waarde aan van het midden van het eerste deelinterval
    x = a + dx / 2 # begin niet bij a maar bij a + de helft van de breedte van een deelinterval, de rest blijft hetzelfde
    for i in range(n):
        som = som + f(x)
        # x neemt de waarde aan van het volgende deelinterval
        x = x + dx
    return dx * som


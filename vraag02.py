
# Combinaties

# Je kan een combinatie op een recursieve manier berekenen via volgende formule:
# C(n, k) = C(n-1, k-1) * n / k
# met als basisgevallen C(0, 0) = 1 en C(n, 0) = 1.

# Schrijf een functie C(n,k) die de combinatie berekent met die formule

def C(n, k):
    if k == 0 or n == k:
        return 1
    return C(n-1, k-1) * n // k
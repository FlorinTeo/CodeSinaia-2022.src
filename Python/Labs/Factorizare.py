print("Primes factorization")
N = 23456789876
f = 2
notFirst = False
print(f"{N} = ", end="")
# iterate through each factor
while f * f <= N:
    p = 0
    while N % f == 0:
        p += 1
        N = int(N / f)
    if p > 0:
        if notFirst:
            print(f" * ", end="")
        print(f"{f}^{p}", end="")
        notFirst = True
    f += 1
if N > 1:
    if notFirst:
        print(f" * ", end="")
    print(f"{N}")
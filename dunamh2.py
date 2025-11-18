def dinamh(x):
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return 2 ** k
        
x=int(input("dwse arithmo"))
dinamh(x)

print(dinamh(x))
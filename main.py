import math

def f():
    # 1-usul: math.ceil(x)
    """
    x ning "ceiling" ni, x dan katta yoki teng eng kichik butun sonni qaytaring.
    Agar x float bo'lmasa, delegatlar "x.__ceil__" ga integral qiymatini qaytarishi kerak.
    """
    x = 3
    print(x.__ceil__())
    print(math.ceil(3))
    print(type(math.ceil(3.14)))

    # 2-usul: math.comb(n, k)
    """
    
    """
    pass

def main():
    f()

if __name__ == "__main__":
    main()

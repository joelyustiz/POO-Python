def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """
    value = None
    
    if n == 1:
        return 1
    
    value = n * factorial(n - 1)
    print(f'value= {value} | n= {n}')
    return value

n = int(input('Escribe un entero: '))

print(factorial(n))
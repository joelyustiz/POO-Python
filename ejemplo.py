def my_func(x):
    respuesta = 0
    for i in range(2000):
        respuesta += 1
    print(respuesta)
    return respuesta

if __name__ == '__main__':
    my_func(1)
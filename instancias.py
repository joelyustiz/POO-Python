
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(3, Coordenada))
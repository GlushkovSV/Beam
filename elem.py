from math import sqrt
import functools

# from node import Node


class Elem:
    Elements = []

    def __init__(self, elemid: int = 0, nodelist: list = None, material: dict = None, Iyy: float = 0):
        self.elemid = elemid
        if not material:
            self.Exx = 2e5
            self.prxy = 0.3
        else:
            self.Exx = material.get('Exx', 2e5)
            self.prxy = material.get('prxy', 0.3)
        self.Iyy = Iyy
        if nodelist:
            self.nodelist = nodelist
        else:
            self.nodelist = list()
        self.Elements.append(self)

    def setmaterial(self, material: dict):
        self.Exx = material.get('Exx', 2e5)
        self.prxy = material.get('prxy', 0.3)

    def setinertia(self, Iyy):
        self.Iyy = Iyy

    @functools.cached_property
    def length(self) -> float:
        return sqrt(pow(self.nodelist[1].coord[0]-self.nodelist[0].coord[0], 2) +
                    pow(self.nodelist[1].coord[1]-self.nodelist[0].coord[1], 2))

    @functools.cached_property
    def stiffnes(self):
        k = self.Exx * self.Iyy / pow(self.length, 3)
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        matrix[0] = [12, 6*self.length, -12, 6*self.length]
        matrix[1] = [6 * self.length, 4*pow(self.length, 2), -6*self.length, 2*pow(self.length, 2)]
        matrix[2] = [-12, -6*self.length, 12, -6*self.length]
        matrix[3] = [6 * self.length, 2*pow(self.length, 2), -6*self.length, 4*pow(self.length, 2)]
        matrix = [[matrix[row][column] * k for column in range(4)] for row in range(4)]
        return matrix

    def __str__(self):
        nl = '\n'.join(str(node) for node in self.nodelist)

        return f'Element ID={self.elemid}\nNodes:\n{nl}\nlen={self.length}\n'

    def setnodes(self, nodelist: list):
        self.nodelist = nodelist

    # @functools.cached_property
    def getindex(self) -> list:
        return [*self.nodelist[0].dof.values(),
                *self.nodelist[1].dof.values()]

    def set_distributed_force(self, q):
        self.nodelist[0].force['Fy'] = q * self.length / 2
        self.nodelist[0].force['Mz'] = q * pow(self.length, 2) / 12
        self.nodelist[1].force['Fy'] = q * self.length / 2
        self.nodelist[1].force['Mz'] = -q * pow(self.length, 2) / 12

    @staticmethod
    def listall():
        for elm in Elem.Elements:
            print(elm)

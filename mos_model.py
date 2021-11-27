import math
import numpy as np


class Nmos33:
    def __init__(self):
        self.u = 35 * 1e-3
        self.tox = 6.65 * 1e-9
        self.cox = 3.9 * 8.854 * 1e-12 / self.tox
        self.k = self.u * self.cox
        self.s = None
        self.lamda = 0.037
        self.vth = 0.695

        self.gm = None
        self.id = None

    def show_para(self):
        print(self.k)


class Pmos33:
    def __init__(self):
        self.u = 9.25 * 1e-3
        self.tox = 6.62 * 1e-9
        self.cox = 3.9 * 8.854 * 1e-12 / self.tox
        self.k = self.u * self.cox
        self.s = None
        self.lamda = 0.008
        self.vth = 0.672

        self.gm = None
        self.id = None

    def show_para(self):
        print(self.k)


n = Nmos33()
p = Pmos33()

n.show_para()
p.show_para()
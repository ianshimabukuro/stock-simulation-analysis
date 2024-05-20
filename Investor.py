import numpy as np
import random


class Investor:
    def __init__(self,name,pp,ip):
        self.name = name
        self.pp = pp
        self.ip = ip


    def evaluate(self,intrinsic_value):
        evaluation = np.random.normal(intrinsic_value, self.evaluation_points, 1)
        return evaluation




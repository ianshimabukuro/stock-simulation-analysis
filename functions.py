from numpy import random

def draw_gaussian(mean,sigma):
    return random.normal(mean,sigma,1)[0]


import torch  
import torch.nn as nn
import torch.nn.functional as F 
import numpy 
import random
import math 

A = 5
T = 20


class Arm():
    def __init__(self, p, T):
       self.prob = p
       self.steps = T
    def gen(self):
        for i in range(self.steps):
            

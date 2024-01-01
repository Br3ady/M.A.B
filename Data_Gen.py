import torch  
import torch.nn as nn
import torch.nn.functional as F 
import numpy 
import random
import math 
import matplotlib.pyplot as plt
import datetime
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

N = 5
T = 200


class Arm():
    def __init__(self):
        pass
    def gen(self,mu, sig):
        spun = numpy.random.normal(mu, sig, T)
        return spun

class Arms():
    def __init__(self, N):
        self.Num = N
        self.arm_probs = {}
        self.tensor = []
    def make_probs(self):
        samples = numpy.random.normal(1,5,self.Num)
        for i, prob in enumerate(samples):
            self.arm_probs[i] = abs(prob)
    def sample(self):
        for i in range(self.Num):

            X=Arm.gen(self.arm_probs[i],.00001,self.Num)
            self.tensor.append(X)
        self.tensor = numpy.array(self.tensor)
        return self.tensor


B = Arms(N)
B.make_probs()
out = B.sample()
plt.imshow(out,cmap='hot')
plt.show()

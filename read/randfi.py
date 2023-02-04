import random
import string
from typing import Any, Union

class number_get():
    I: float = 0.0
    def __init__(self):
        self.k = 10
        self.I = random.randint(0, 5)
        self.F = self.k * self.I

    def get(self):
        self.I = random.uniform(0.0, 5.0)
        self.F = self.k * self.I
        alien = {'F': self.F, 'I': self.I}
        return alien
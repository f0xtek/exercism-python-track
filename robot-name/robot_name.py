import random
import string
from time import time


class Robot(object):
    def __init__(self):
        self.name = self.generate()

    def generate(self):
        random.seed(time())
        letters = "".join(random.choice(string.ascii_letters).upper() for x in range(random.randint(2, 2)))
        digits = random.randint(100, 999)
        return letters + str(digits)

    def reset(self):
        self.__init__()

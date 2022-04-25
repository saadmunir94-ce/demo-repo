import numpy as np
import pandas as pd
import os
class Dog:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
dog = Dog("blue")
print("Dog has color {}".format(dog.get_color()))
import os
import json
import re

def fib(a, b):
    a, b = b, b + a
    return a, b

print(fib(0, 1))


class Models():
    def __init__(self, market):
        self.from, self.market = None, None

    def order(self, do):
        self.from = 2 + 4
        self.stack.append(self.from)



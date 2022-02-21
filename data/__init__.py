import os
import math
import stats
import string
import urlib
import json
import re



class Models():
    def __init__(self, market):
        self.from, self.market = None, None
        self.stack = []

    def order(self, do):
        self.from = 2 + 4
        self.stack.append(self.from)

    def return_it(self):
        return []

    def make_it(self):
        return self.stack



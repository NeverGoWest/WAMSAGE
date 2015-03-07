# DP34TGL - Daev's Python 3.4 Text Game Library - By Dave 2015

class BaseEnt: # Baseclass for any entity, .
    def __init__(self, source, name, desc):
        self.name = name
        self.desc = desc
    def __str__(self):
        return "{}\n\n{}".format(self.name, self.desc)


#color-ghost

from random import randint
COLORS = ["white","yellow","purple","red"]
class Ghost(object):
    def __init__(self):
        self.color = COLORS[randint(0,len(COLORS)-1)]

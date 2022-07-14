"""
Consider an intelligent traffic signal. The signal has two states: red and
green. The vehicle density in front of the signal is denoted by the variable v.
If the vehicle density crosses a threshold T in either direction, the state of
the signal changes. The dynamics of this change is represented in the image
given below:
"""


class Signal():
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = T

    def sense(self, v):
        self.v = v

    def update(self):
        if self.state == 'red':
            if self.v < self.T:
                self.state = 'red'
            elif self.v >= self.T:
                self.state = 'green'
        elif self.state == 'green':
            if self.v < self.T:
                self.state = 'red'
            elif self.v >= self.T:
                self.state = 'green'

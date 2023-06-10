import numpy as np

class Environment:
    def __init__(self, size, agent_start=[0,0]):
        self.size = size
        self.agent_location = agent_start

    def step(self, action):
        x, y = self.agent_location
        if "left" in action:
            self.agent_location[1] = max(self.agent_location[1] - 1, 0)
        elif "right" in action:
            self.agent_location[1] = min(self.agent_location[1] + 1, self.size - 1)
        elif "up" in action:
            self.agent_location[0] = max(self.agent_location[0] - 1, 0)
        elif "down" in action:
            self.agent_location[0] = min(self.agent_location[0] + 1, self.size - 1)
        elif "noop" in action:
            pass

    def get_state(self):
        return self.agent_location

    def __repr__(self):
        s = ""
        for i in range(self.size):
            for j in range(self.size):
                if [i,j] == self.agent_location:
                    s += "X"
                else:
                    s += " "
            s += "\n"
        return s
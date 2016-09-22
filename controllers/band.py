

class Band:
    def __init__(self, model):
        self.model = model

    def set_path(self, path):
        self.model.path = path

    def update(self):
        if self.model.path:
            self.update_pos()
        # add random game events

    def update_pos(self):
        assert self.model.path

        leader = self.model.leader
        goal = self.model.path[0]
        x, y = self.model.pos
        a = abs(x - goal[0])**2
        b = abs(y - goal[1])**2
        distance = sqrt(a + b)
        factor = leader.speed / distance
        dx, dy = goal[0] * factor, goal[1] * factor
        self.model.last_pos = (x, y)
        self.model.pos = x + dx, y + dy



from math import hypot


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
        distance_x = x - goal[0]
        distance_y = y - goal[1]
        total_distance = hypot(distance_x, distance_y)
        tick_distance = leader.speed
        if total_distance < tick_distance:
            tick_distance = total_distance
            self.model.path.pop(0)
        factor = tick_distance / total_distance
        dx, dy = distance_x * factor, distance_y * factor
        self.model.last_pos = (x, y)
        self.model.pos = x + dx, y + dy

from play import Lab

from actor import Actor


class Enemy(Actor):
    def update(self, lab: Lab, target: tuple[int, int], time: float, speed: float) -> None:
        if time % speed == 0:
            next_position = self.find_step(target, lab)
            self.set_position(next_position)

    def find_step(self, target: tuple[int, int], lab: Lab) -> tuple[int, int]:
        INF = 1000
        start = self.get_position()
        x, y = self.get_position()
        distance = [[INF] * lab.w for _ in range(lab.h)]
        distance[y][x] = 0
        prev = [[None] * lab.w for _ in range(lab.h)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < lab.w and 0 < next_y < lab.h and \
                        lab.is_free((next_x, next_y)) and distance[next_y][next_x] == INF:
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = target
        if distance[y][x] == INF or start == target:
            return start
        while prev[y][x] != start:
            x, y = prev[y][x]
        return x, y

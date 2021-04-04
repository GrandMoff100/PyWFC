from .state import Potential


def coordgen(w,h):
    for x in range(w):
        for y in range(h):
            yield x,y


class Wave:
    def __init__(self, dims: tuple, states: tuple):
        self.dims = dims
        self.states = states
        w, h = dims
        self._grid = [[Potential(self.states) for x in range(w)] for y in range(h)]

    def pos(self, x: int, y: int) -> Potential:
        try:
            return self._grid[y][x]
        except IndexError:
            return Potential(self.states)

    def getstate(self, id: str):
        for state in filter(lambda x: x.name == id, self.states):
            return state

    def gridmin(self):
        """minimum = None
        for x,y in coordgen(*self.dims):
            count = self._grid[y][x].count(self, (x, y))
            if count:
                if minimum is None or count < minimum[1]:
                    minimum = [(x, y), count]   
        return minimum
        """
        count = lambda p: self._grid[p[1]][p[0]].count(self, p)
        items = sorted(filter(count, coordgen(*self.dims)), key=count)
        return (items[0], count(items[0])) if items else None
        
    def collapse(self, presets: dict = {}):
        minimum = self.gridmin()
        while minimum:
            self.pos(*minimum[0]).collapse(self, minimum[0])
            minimum = self.gridmin()
        return self._grid


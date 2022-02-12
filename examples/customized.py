from pathlib import Path
from gridview import GridView

grid = [
    ['Month', 'Cost', 'Notes'],
    ['January', 12.33],
    ['February', 33.10],
    ['March', 54.30, 'Delayed.'],
    ['April', 22.12],
    ['May', 31.41],
    ['June', 41.36, 'Delayed.'],
    ['July', 22.23, 'Lost!'],
    ['August', 82.10],
    ['September', 20.01, 'Replaced.'],
    ['October', 55.20],
    ['November', 34.23],
    ['December', 33.52]]

class Report(GridView):
    transpose = True

    def text(self, e, x, y):
        if x == 1 and y > 0:
            return f'${e}'
        return str(e)

    def color(self, e, x, y):
        if y == 0:
            return 'lightgray'
        if x == 0:
            return 'lightyellow'
        if x == 1:
            if e > 50:
                return '#8888ff:too high'
            if e < 20:
                return '#ffff88:too low'
        if x == 2:
            if e.endswith('!'):
                return '#ff8888'
        return None

svg_path = Path(__file__).with_suffix('.svg')
Report(grid).save(svg_path)

from pathlib import Path
from gridview import GridView

class Animal:
    def __init__(self, name):
        self._name = name
        
    def __str__(self):
        return self._name
        
    def color(self):
        return 'lightgreen'
        
class Person:
    def __init__(self, name, *, male):
        self._name = name
        self._male = male

    def __str__(self):
        title = 'Sir' if self._male else 'Madame'
        return f'{title}\n{self._name}'

    def color(self):
        return 'lightblue'

grid = [['']*5 for n in range(6)]
grid[0][2] = Animal('Ozzy')
grid[4][1] = Animal('Axel')
grid[2][3] = Person('Susana', male=False)
grid[4][0] = Person('Tom', male=True)
grid[5][4] = Person('James', male=True)

class Report(GridView):
    flip_x = True
    default_color = '#ffffaa'

    def color(self, e, x, y):
        return e.color()

svg_path = Path(__file__).with_suffix('.svg')
Report(grid).save(svg_path)

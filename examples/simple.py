from pathlib import Path
from gridview import GridView

grid = [[1,2,3], [4, 5], [6, 7, 8, 9]]

svg_path = Path(__file__).with_suffix('.svg')
GridView(grid).save(svg_path)

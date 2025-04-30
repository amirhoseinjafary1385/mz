

class Cell(object):
    def __init__(self, name):
        self.name=name


class Grid(object):
    def __init__(self, col_amount, row_amount):

        self.cell_list = [] # empty list to hold all cells

        for col in range(col_amount):
            for row in range(row_amount):
                # create each cell as instance of Cell,
                # with the concatenated col and row numbers
                # as the name, then add the cell.name to cell_list
                cell = Cell(str(col) + '_' + str(row))
                self.cell_list.append(cell.name)


grid = Grid(10,10) # make an instance of Grid with size 10x10
print (grid.cell_list)
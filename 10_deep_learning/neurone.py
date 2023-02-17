# -*- coding: utf-8; mode: python -*-

class neurone(object):
    cells_linked = []
    weight = 100

    def __init__ (self, cell_weight, other_cells):
        '''init by declaring linked cells'''
        for cell in other_cells:
            cells_linked.append(cell)
        weight = cell_weight
    
    def signal():
        '''collect signals from all linked cells'''
        for cell in cells_linked:
            result += cell.weight*cell.signal
    

# image en mode point
image
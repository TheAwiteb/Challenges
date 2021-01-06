##Crop Fields

#You're given a 2D list / matrix of a crop field. Each crop needs a water source. Each water source hydrates the 8 tiles around it
#With "w" representing a water source, and "c" representing a crop, is every crop hydrated?

##Examples

"""
crop_hydrated([
  [ "w", "c" ],
  [ "w", "c" ],
  [ "c", "c" ]
]) ➞ True

crop_hydrated([
  [ "c", "c", "c" ]
]) ➞ False
# There isn"t even a water source.

crop_hydrated([
  [ "c", "c", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "c", "c", "c", "c" ],
  [ "c", "w", "c", "c" ]
]) ➞ False
"""
##Notes
#"w" on its own should return True, and "c" on its own should return False.

def crop_hydrated(field):
    max_x = len(field[0]) - 1
    max_y = len(field) - 1
    whaters_positions = []
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if field[y][x] == 'w':
                whaters_positions.append({"x":x, "y":y})
    if len(whaters_positions) == 0:
        return False
    else:
        for position in whaters_positions:
            x = position['x']
            y = position['y']
            for i in [-1,1]:
                try:
                    if field[y][x + i] == 'c':
                        field[y][x + i] = ''
                except:
                    pass
                try:
                    if field[y+i][x] == 'c':
                        field[y+i][x] = ''
                except:
                    pass
                try:
                    if field[y+i][x+i] == 'c':
                        field[y+i][x+i] = ''
                except:
                    pass
                try:
                    if field[y+1][x-1] == 'c':
                        field[y+1][x-1] = ''
                except:
                    pass
                try:
                    if field[y-1][x+1] == 'c':
                        field[y-1][x+1] = ''
                except:
                    pass
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if field[y][x] == 'c':
                return False
            else:
                pass
    return True
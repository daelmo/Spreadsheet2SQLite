
def Point_is_in_Range(cell, start, end):
    cellX = str(cell[0])
    cellY = int(cell[1])
    startX = str(start[0])
    startY = int(start[1])
    endX = str(end[0])
    endY = int(end[1])

    if cellY >= startY and cellY <= endY:
        if len(startX) < len(cellX) < len(endX):
            return 1
        if len(cellX) < len(endX) and len(cellX) == len(startX):
            if cellX >= startX: return 1
        if len(cellX) > len(startX) and len(cellX) == len(endX):
            if cellX <= endX: return 1
        if len(cellX) == len(startX) == len(endX):
            if cellX >= startX or cellX <= endX: return 1
        return 0

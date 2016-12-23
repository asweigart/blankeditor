import doctest

def isPointInsideRect(px, py, rect):
    """Returns true if the point's coordinates (`px` and `py`) are inside the rectangle `rect`.

    >>> isPointInsideRect(5, 5, {'x1': 0, 'y1': 0, 'x2': 10, 'y2': 10})
    True
    >>> isPointInsideRect(-2, -2, {'x1': 0, 'y1': 0, 'x2': 10, 'y2': 10})
    False
    >>> isPointInsideRect(-2, 5, {'x1': 0, 'y1': 0, 'x2': 10, 'y2': 10})
    False
    """
    return (rect['x1'] < px < rect['x2'] or rect['x1'] > px > rect['x2']) and \
        (rect['y1'] < py < rect['y2'] or rect['y1'] > py > rect['y2'])

def getArea(rect):
    """Returns the area of the `rect` rectangle object.
    >>> getArea({'x1': 0, 'y1': 0, 'x2': 10, 'y2': 10})
    100
    >>> getArea({'x1': -10, 'y1': -10, 'x2': 10, 'y2': 10})
    400
    >>> getArea({'x2': -10, 'y2': -10, 'x1': 10, 'y1': 10})
    400
    """
    width = abs(rect['x1'] - rect['x2'])
    height = abs(rect['y1'] - rect['y2'])
    return width * height

def getOverlapArea(rect1, rect2):
    """Returns the area of the overlapping section of two rectangles.

    >>> getOverlapArea({'x1': -4, 'y1': 4, 'x2': -0.5, 'y2': 2}, {'x1': 0.5, 'y1': 1, 'x2': 3.5, 'y2': 3})
    0
    >>> getOverlapArea({'x1': 0.5, 'y1': 1, 'x2': 3.5, 'y2': 3}, {'x1': -4, 'y1': 4, 'x2': -0.5, 'y2': 2})
    0
    >>> getOverlapArea({'x1': 0, 'y1': 0, 'x2': 1, 'y2': 1}, {'x1': -10, 'y1': -10, 'x2': 10, 'y2': 10})
    1
    >>> getOverlapArea({'x1': -10, 'y1': -10, 'x2': 10, 'y2': 10}, {'x1': 0, 'y1': 0, 'x2': 1, 'y2': 1})
    1
    """

    # ensure that x1, y1 is the top-left corner and x2, y2 is the bottom-right corner
    #
    #    x1, y1 +-----------+
    #           |           |
    #           |           |
    #           +-----------+ x2, y2
    #
    if rect1['x1'] > rect1['x2']:
        rect1['x1'], rect1['x2'] = rect1['x2'], rect1['x1']
    if rect1['y1'] < rect1['y2']:
        rect1['y1'], rect1['y2'] = rect1['y2'], rect1['y1']

    if rect2['x1'] > rect2['x2']:
        rect2['x1'], rect2['x2'] = rect2['x2'], rect2['x1']
    if rect2['y1'] < rect2['y2']:
        rect2['y1'], rect2['y2'] = rect2['y2'], rect2['y1']




    # handle case of zero points inside the other rectangle
    if not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect2['x1'], rect2['y1'], rect1) and \
       not isPointInsideRect(rect2['x2'], rect2['y2'], rect1) and \
       not isPointInsideRect(rect2['x1'], rect2['y2'], rect1) and \
       not isPointInsideRect(rect2['x2'], rect2['y1'], rect1):       
        return 0

    # handle case of one point inside the other rectangle
    #   top-left (x1, y1) corner of rect1 is inside rect2
    if isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2):
        return getArea({'x1': rect1['x1'], 'y1': rect1['y1'], 'x2': rect2['x2'], 'y2': rect2['y2']})

    #   bottom-right (x2, y2) corner of rect1 is inside rect2
    if isPointInsideRect(rect1['x2'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2):
        return getArea({'x1': rect2['x1'], 'y1': rect2['y1'], 'x2': rect1['x2'], 'y2': rect1['y2']})

    #   top-right (x2, y1) corner of rect1 is inside rect2
    if isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2):
        return getArea({'x1': rect2['x1'], 'y1': rect2['y2'], 'x2': rect1['x2'], 'y2': rect1['y1']})

    #   bottom-left (x1, y2) corner of rect1 is inside rect2
    if isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2):
        return getArea({'x1': rect2['x2'], 'y1': rect2['y1'], 'x2': rect1['x1'], 'y2': rect1['y2']})

    # handle case of two points inside the other rectangle
    #   handle if top two points of rect1 are in rect2
    if isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2):
        return getArea({'x1': rect1['x1'], 'y1': rect1['y1'], 'x2': rect1['x2'], 'y2': rect2['y2']})

    #   handle if bottom two points of rect1 are in rect2
    if isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       isPointInsideRect(rect1['x2'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2):
        return getArea({'x1': rect1['x1'], 'y1': rect2['y1'], 'x2': rect1['x2'], 'y2': rect1['y2']})


    #   handle if left two points of rect1 are in rect2
    if isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       isPointInsideRect(rect1['x1'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x2'], rect1['y2'], rect2):
        return getArea({'x1': rect1['x1'], 'y1': rect1['y1'], 'x2': rect2['x2'], 'y2': rect1['y2']})

    #   handle if right two points of rect1 are in rect2
    if isPointInsideRect(rect1['x2'], rect1['y1'], rect2) and \
       isPointInsideRect(rect1['x2'], rect1['y2'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and \
       not isPointInsideRect(rect1['x1'], rect1['y2'], rect2):
        return getArea({'x1': rect2['x1'], 'y1': rect1['y1'], 'x2': rect1['x2'], 'y2': rect1['y2']})



    # handle case of four points inside the other rectangle
    if isPointInsideRect(rect1['x1'], rect1['y1'], rect2) and isPointInsideRect(rect1['x2'], rect1['y2'], rect2):
        return getArea(rect1)
    

    return getOverlapArea(rect2, rect1)


doctest.testmod()
getOverlapArea({'x1': -4, 'y1': 4, 'x2': -0.5, 'y2': 2}, {'x1': 0.5, 'y1': 1, 'x2': 3.5, 'y2': 3})

inp1_r1 = {'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2}
inp1_r2 = {'x1': 1, 'y1': 1, 'x2': 3, 'y2': 3}
print(getOverlapArea(inp1_r1, inp1_r2))

inp2_r1 = {'x1': -3.5, 'y1': 4, 'x2': 1, 'y2': 1}
inp2_r2 = {'x1': 1, 'y1': 3.5, 'x2': -2.5, 'y2': -1}
print(getOverlapArea(inp2_r1, inp2_r2))

inp3_r1 = {'x1': -4, 'y1': 4, 'x2': -0.5, 'y2': 2}
inp3_r2 = {'x1': 0.5, 'y1': 1, 'x2': 3.5, 'y2': 3}
print(getOverlapArea(inp3_r1, inp3_r2))


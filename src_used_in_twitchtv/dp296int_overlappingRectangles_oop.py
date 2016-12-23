import doctest

class Rect():
    def __init__(self, coordinateString):

        # `coordinateString` is formatted as '1,2 6,7'
        self.topleft, self.bottomright = coordinateString.split(' ')
        self.left, self.top = self.topleft.split(',')
        self.left = int(self.left)
        self.top = int(self.top)

        self.right, self.bottom = self.bottomright.split(',')
        self.right = int(self.right)
        self.bottom = int(self.bottom)

        # ensure that self.top is above self.bottom & self.left is to the left of self.right
        if self.left > self.right:
            self.left, self.right = self.right, self.left
        if self.bottom > self.top:
            self.bottom, self.top = self.top, self.bottom

        # set the corner member variables
        self.topleft = (self.left, self.top)
        self.bottomright = (self.right, self.bottom)
        self.topright = (self.right, self.top)
        self.bottomleft = (self.left, self.bottom)

        self.width = self.right - self.left
        self.height = self.top - self.bottom

        #self.cornerIteration = 0


    def getArea(self):
        return self.width * self.height

    def containsPoint(self, point):
        x, y = point
        return self.left < x < self.right and self.bottom < y < self.top

    def containsRect(self, rect):
        pass


    '''
    def __iter__(self):
        return self

    def __next__(self):
        if self.cornerIteration == 4:
            self.cornerIteration = 0
            raise StopIteration

        self.cornerIteration += 1

        if self.cornerIteration == 1:
            return self.topleft
        elif self.cornerIteration == 2:
            return self.topright
        elif self.cornerIteration == 3:
            return self.bottomright
        elif self.cornerIteration == 4:
            return self.bottomleft
    '''


    def getOverlapArea(self, otherRect):
        pass
        # handle case where zero corners of otherRect are in this rectangle.
        


        # handle case where one corner of otherRect are in this rectangle.



        # handle case where two corners of otherRect are in this rectangle.


        # handle case where four corners of otherRect are in this rectangle.




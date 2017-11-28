class Square:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo):
        return (squareOne.side * 4) + (4 * squareTwo.side)

squareOne = Square(5) # 5*4
squareTwo = Square(10) # 10 * 4

print("Sum of sides of both th squares = ", squareOne + squareTwo)

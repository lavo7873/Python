class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
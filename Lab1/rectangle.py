class Rectangle(object):
    """ Rectangle class """
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
    
    def __str__(self):
        return "\n".join(["#" * self.width for _ in range(self.height)])
    
    def area(self):
        "area"
        return(self.width * self.height)
    
    def perimeter(self):
        "perimeter"
        return(2 * self.width + 2 * self.height)
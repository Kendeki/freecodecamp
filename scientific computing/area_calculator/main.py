class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    
    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

    def set_width(self, num: int):
        self._width = num
    
    def set_height(self, num: int):
        self._height = num
    
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    
    def get_diagonal(self):
        return ((self._width)**2 + (self._height)**2)**(1/2)

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        return ''.join(["*" * self._width + '\n' for _ in range(self._height)]) 
    
    def get_amount_inside(self, other: 'Rectangle'):
        return int((self._width / other._width) * (self._height / other._height))


class Square(Rectangle):
    def __init__(self, length: int):
        Rectangle.__init__(self, length, length)

    def __str__(self):
        return f'Square(side={self._height: int})'

    def set_side(self, num: int):
        self._height = num
        self._width = num

    def set_width(self, num: int):
        self._height = num
        self._width = num
    
    def set_height(self, num: int):
        self._height = num
        self._width = num
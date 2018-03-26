
class Rectangle:
  length = 0
  width = 0
  
  def __init__(self,length,width):
    self.length = length
    self.width = width
    self.ValidateDimension()
  
  def ValidateDimension(self):
    if (self.length.isnumeric() and self.width.isnumeric )== False
      raise ValueError("The parameter is not  numeric")
      
  
  def area(self):
    return self.length*self.width
    
    def perimeter(self):
      return 2*(self.length + self.width)
input = ("What is the length")
input = ("What is the width")
      
small = Rectangle ("9","6") 
invalid = Rectangle ("fixe",5)
print(invalid.area())
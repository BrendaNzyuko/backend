class Taxpayer:
  income = 0
  name = "Brenda"
  def __init__ (self,name,icome):
    self.income=icome
    self.name = name
    self.minimum = minimum
    self.ValidateIncome()
    self.ValidateName()
    self.ValidateMinimum()
    
  def ValidateIncome(self):
    if self.income.isnumeric()== False:
     raise ValueError("The income {} is not numeric".format(self.income))
     
     def ValidateName(self):
       if self.name.string():
        raise ValueError("The name{} is not a string".format(self.name))
        
     def ValidateMinimum(self):
        if flaot(self.income) <10000:
          raise ValueError("The income{}is below minimum ")
     
  def calculate_tax(self):
    return float(self.income)*0.3
    
income = input("What is the income")
name = input ("What is your name?")
employee = Taxpayer(name,income,minimum)
print(employee.calculate_tax())
    
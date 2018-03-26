def welcome_student(name):
   welcome_str= "Hi {} welcome to Akirachix"
   return welcome_str.format(name)
   
name=input("Enter name")
print(welcome_student(name))
print(welcome_student ("Brenda"))
print(welcome_student ("Joyce"))
print(welcome_student ("Farida"))
  
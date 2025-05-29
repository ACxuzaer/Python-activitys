# create class
class IOString():

    # constructor to set dafault value
   def _init_(self):
      self.syr1 = ""


      # funtion to get input form user
   def get_string(self):
      self.str1 = input("Enter String : ")


      # funtion to print the string in upper case
   def print_string(self):
      print("Result is :", self.str1.upper())


# Object creation
str1 = IOString()


# Call funtions
str1.get_string()
str1.print_string()
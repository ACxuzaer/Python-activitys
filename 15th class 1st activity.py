# To write in a file using with ()funtion
with open('Codingal.txt','w') as file:
  file.write("Hi! I am penguin and i am 1 yr old.")
file.close()

# split the files into words
with open('Codingal.txt','r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()
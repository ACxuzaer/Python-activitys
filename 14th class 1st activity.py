#open file and read its contents overthere
file = open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginging 8 charecters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('Codingal.txt','a')
file.write(" Hi! I am a Penguin and i am 1 years old")
file.close()
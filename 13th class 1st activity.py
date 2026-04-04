# Write mode (creates file or overwrites content)

file_write = open("Microsoft Word Document (.docx)", "w")

file_write.write("File in write mode...\n")

file_write.write("Hi! I am Penguin. I am 1 yr old.\n")

file_write.close()

# Read mode

file_read = open("Microsoft Word Document (.docx)", "r")

print("Reading the file after write:\n")

print(file_read.read())

file_read.close()

# Append mode (adds new content without deleting old content)

file_append = open("Microsoft Word Document (.docx)", "a")

file_append.write("\nFile in append mode...\n")

file_append.write("Penguins love cold places.\n")

file_append.close()

# Read again to see appended content

file_read = open("Microsoft Word Document (.docx)", "r")

print("\nReading the file after append:\n")

print(file_read.read())

file_read.close()
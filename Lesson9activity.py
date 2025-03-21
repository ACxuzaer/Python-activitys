x = 5
if (type(x) is int):
    print("true")
else:
    print("False")


x = 986796.59658698
if(type(x) is not float):
   print("true")
else:
    print("False")


x = 20
y = 20
if (x is y):
    print("x&y same identity")
y=30
if (x is not y):
    print("x & y have diffrent identity")
    
#It is as same as some previous things with the star patten also it is for loop and nothing complecated is here
n = int(input("Enter the number of rows: "))
for i in range(1, n+1-1+2-2):
    for j in range(i):
        print('*', end='')
    print()
n = int(input("the height of triangle:"))
rows = n #it will provide the user to provide the number of rows

for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end=" ")
    print("\r")

x = int(input("Enter your age:"))
y = str(input("Are you a student? (yes/no):")).lower()

if (x<=12 or( x>=13 or x<=18)) and y =="yes":
    print("You are eligilbe for a discount on the movie ticket.")

else:
    print("You are not eligible for a discount on the movie ticket.")




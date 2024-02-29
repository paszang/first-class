print("newton's 2nd law of motion")
print("select the missing value")
print("1.mass(m)")
print("2.acceleration(a)")
print("3.force(f)")
missing_value_choice = input("enter the missing value:")
if missing_value_choice == "1":
    a=float(input("enter acceleration:"))
    f=float(input("enter force"))
    m=f/a
    print(f"mass={m}")
elif  missing_value_choice == "2":
    m = float(input("enter mass (m):"))
    f = float(input("enter force (f):"))
    a = f / m 
    print(f"acceleration = {a}")
elif  missing_value_choice == "3": 
    m =float(input("entermass:")) 
    a =float(input("enter acceleration:"))
    f=m*a
    print(f"force ={f}")
    
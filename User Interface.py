Name = input("Enter your name: ")
print(f"Hello {Name}")
Age = int(input("Enter your age: "))
if Age >= 18:
 print("You are an adult")
elif Age < 0:
 print("You're not born yet")
elif Age == 0:
  print("You were just born")
elif Age >= 13:
  print("You are a teen")
else:
    print("You are a kid")
Birth_Date = input("Enter the date were you born: ")
print(f"You were born in {Birth_Date}")
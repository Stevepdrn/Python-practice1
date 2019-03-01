rating = input("Enter movie rating (G, PG, PG-13, R or NC-17): ")
age = eval (input("What's your age? "))
if rating == "G":
    print("You may see that movie!")
    
if rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
        
if rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

if rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

if rating == "NC-17":
    print("You may not see that movie!")

else:
  print("Sorry, enter a supported movie rating")
    
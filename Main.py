# Nick Troiano
# A Baseball Trivia Game

totalCorrect = 0

print("Welcome to my baseball trivia game!!")

x = input("Would you like to attempt baseball trivia?")
if x == "yes" or x == "Yes":
    print("Good Luck!")
elif x == "no" or x == "No":
    exit(0)
y = input("Who won the World Series in 2018?")
if y == "Chicago Cubs" or y == "Cubs" or y == "chicago cubs" or y == "cubs" or y == "chicago" or y == "Chicago":
    print("Congratulations, next question.")
    totalCorrect += 1
    y = input("How many World Series have the New York Yankees won?")
    if y == "27":
        print("Correct, here comes question 3.")
        y = input ("Who owns the record for most career stolen bases?")
        if y == "Ricky Henderson" or y == "ricky henderson":
            print("Good job, next question")
            y = print("Who was the first african american player in the MLB?")
            if y == "Jackie Robinson" or y == "jackie robinson":
                print("Amazing! Next question.")
                y = input ("Who was the first baseball player to have his number retired?")
                if y == "Lou Gehrig" or y == "lou gehrig":
                    print("Congratulations, you made it to the end")




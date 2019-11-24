# Nick Troiano
# A Baseball Trivia Game

# Defining Score variables.
x = 0
score = x

# Question One
print("Who won the world series in 2018?")
answer_1 = input("a)Yankees\nb)Cubs\nc)Astros\nd)Rockies\nYour Answer:")
if answer_1.lower() == "b" or answer_1.lower() == "Cubs" or "cubs":
    print("Correct, next question.")
    x = x + 1
else:
    print("Incorrect, the Cubs won their first world series in 2018.")

# Question Two
print("How many World Series have the New York Yankees won?")
answer_2 = input("a)14\nb)34\nc)27\nd)28\nYour Answer:")
if answer_2.lower() == "c" or answer_2.lower() == "27":
    print("Correct, next question.")
    x = x + 1
else:
    print("Incorrect, the yankees have won 27 world series titles.")

# Question Three
print("True or False? Ricky Henderson owns the record for most career stolen bases.")
answer_3 = input("Your Answer:")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct, next question.")
    x = x + 1
else:
    print("Incorrect, Ricky Henderson does own the record for the most career stolen bases.")

# Question Four
print("When was the last time the Philadelphia Phillies won the world series?")
answer_4 = input("a)2008\nb)2015\nc)1987\nd)1994\nYour Answer:")
if answer_4.lower() == "a" or answer_4 == "2008":
    print("Correct, next question")
    x = x + 1
else:
    print("Incorrect, The last time the Philadelphia Phillies won the World Series was 2008")

# Question Five
print("True or False? Jackie Robinson was the first player to have his jersey retired.")
answer_5 = input("Your Answer:")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Congratulations, you have reached the end of the game.")
    x = x + 1
else:
    print("Incorrect, Lou Gherig was the first player to have his jersey retired.")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
#integers represent whole numbers
""" age: 14
#Floats represent decimals
wallet=5.45
#boolean represents true or false, used in evaluations
graduated = false 

def add(x,y):
    print(x+y)
#input asks the user a question and store their responses as a value
bill = float(input("what was the bill?")) """
#print(type(bill))
#add(40, bill)

#lists
""" students = ["Joanna", "Deivid", "David", "other David", "Ethan"]
#similar to saying for i in range(5): print9students[i})]
#print(students[4])
for student in students:
    print(student) 
moneys = [1,2,3,4,5,6]
total = 0
for money in moneys:
    total=total+money
    print(total) """
""" values = [1,2.23,5,7,2,30,15]
#print(values)
 for i in values:
    print(i) 
print(values[0])
print(values[6]) """
#python

""" def sentence(input):
    print(input)
sentence("type") """
# Accept user input
"""x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)"""
#answer will be the variable that is the input, gets split into variable (word) and the len() says how many words there are with print
""" answer = input("Please enter a sentence: ")
words = answer.split()
print(len(words)) """
#MADLIBS PROJECT
""" noun_1 = input("type a noun: ")
noun_2 = input("type another noun: ")
verb_1 = input("type a verb: ")
verb_2 = input("type another verb: ")
verb_3 = input("type another verb: ")
adj_1 = input("type a adjective: ")
adj_2 = input("type another adjective: ")
adv = input("type an adverb: ")
feeling = input("type an emotion: ")
celeb = input("name a celebrity: ")
number = input("type a number: ")
pronoun = input("type a pronoun: ")
print(f"I was so {feeling} when my favorite person, {celeb} showed up to my {adj_1} school. They were so {adj_2} when they {verb_1}  next to me! I couldn't help but {adv} {verb_2} with a {noun_1}. When they left, they {verb_3} my school {number} {noun_2}s.")
 """





""" def login(password):
    #if the statement is true then go to next line
    if password == "secret":
        print("logged in")
    else:
        print("password incorrect")
#x = input("whats the password")
#login(x)

def grade(score):
    if score >=92:
        print("A")
        #use elif, bc it means that if the conditions of the if above it are met it wont be ran
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F") """
#score = int(input("what the score"))
#grade(score)

""" def gamble(age, id):
    if age >= 21:
        if id:
            print("gamble away")
        else:
            print("You need an id")
    else:
        print("go away ur too young") """
""" 
def gamble(age, id):
    if age >= 21 and id == true:
        print('have fun')
    elif age>= 21 and id== false:
        print("you need an id")
    else:
        print("youre too young")
age = 21
id = true """
def oe(number):
 if (number % 2) == 0:
    print("Even number")
 else:
    print ("Odd number")
number = int(input("type a number to see if it is odd or even: "))
oe(number)

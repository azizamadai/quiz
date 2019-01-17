# this is going to be a 10 question quiz built off of "question.py"
# that gives the user 4 options per question

global score
score = int(0)

def run_quest(quest, ansU, check, ansR):
    print(quest)
    while check == False:
        try:
            print(" ")
            ansU = int(input("Please indicate your answer by selecting a number from 1-4 >  "))
            if ansU == ansR:
                print("Alright, got it.")
                print(" ")
                print("-------------------------------------------------------------------")
                global score
                score = score + 1
                check = True
            elif 0 < ansU < 5:
                print(" ")
                print("-------------------------------------------------------------------")
                print("Alright, got it.")
                check = True
            else:
                print(" ")
                print("You can only choose a number between 1 to 4! ")
        except ValueError:
            print(" ")
            print("You need to write a whole number...!")
                
#------------------------------------------------------------------------------
# FIRST QUESTION DATA

c1 = False
a1 = int(0)
q1 = str("""Hello! Today we are going to take a little history quiz!

Who was the third president of the United States?

1. William Henry Harrison
2. Thomas Jefferson
3. John Quincy Adams
4. Martin Van Buren""")

run_quest(q1, a1, c1, 2)

#------------------------------------------------------------------------------
# SECOND QUESTION DATA

print(" ")
c2 = False
a2 = int(0)
q2 = str("""What was the main cause of the French and Indian War (1754-1763)?

1. Disputed land claims near the Ohio River
2. Conflicts between American colonists and the French over control of the Great Plains
3. Taxation of American colonists without representation in Parliament
4. Violation of trade agreements between European nations and Indians""")

run_quest(q2, a2, c2, 1)

#------------------------------------------------------------------------------
# THIRD QUESTION DATA

print(" ")
c3 = False
a3 = int(0)
q3 = str("""Do you even like history?

1. Yeah, I guess
2. ABSOLUTELY
3. Nah, not really
4. I hate history""")

run_quest(q3, a3, c3, 2)

#------------------------------------------------------------------------------
# FOURTH QUESTION DATA

print(" ")
c4 = False
a4 = int(0)
q4 = str("""Women played an important role during the American Revolutionary war because they...

1. Provided much of the financial backing for the colonial cause
2. Wrote influential articles in colonial newspapers
3. Provided clothing and blankets for the frozen troops at Valley Forge
4. Maintained economic stability in the colonies by managing the households and estates""")

run_quest(q4, a4, c4, 4)

#------------------------------------------------------------------------------
# FIFTH QUESTION DATA

print(" ")
c5 = False
a5 = int(0)
q5 = str("""In what ways do you think history helps us?

1. It doesn't
2. It allows us to make better decisions
3. Helps us develop a better understanding of our world, ourselves, and others
4. Aids us in developing a new level of appreciation for everything, basically""")

while c5 == False:
        try:
            #print(" ")
            print(q5)
            a5 = int(input("Please indicate your answer by selecting a number from 1-4 >  "))
            if a5 == 2 or a5 == 3 or a5 == 4:
                print("Alright, got it.")
                #global score
                score = score + 1
                c5 = True
            elif 0 < a5 < 5:
                print("Alright, got it.")
                c5 = True
            else:
                print(" ")
                print("You can only choose a number between 1 to 4! ")
        except ValueError:
            print(" ")
            print("You need to write a whole number...!")

#------------------------------------------------------------------------------
# SIXTH QUESTION DATA
##
##print(" ")
##c6 = False
##a6 = int(0)
##q6 = str("""The phrase 'Let them eat cake!' is often attributed to who?
##
##1. Susan B. Anthony
##2. Marie Curie
##3. Marie Antoinette
##4. Ada Lovelace""")
##
##run_quest(q6, a6, c6, 3)

print(" ")
print("-------------------------------------------------------------------")
print(" ")
print("You got a...", score * 20, "% on this quiz!")

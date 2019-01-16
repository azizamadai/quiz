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
                global score
                score = score + 1
                check = True
            elif 0 < ansU < 5:
                print("Alright, got it.")
                check = True
            else:
                print(" ")
                print("You can only choose a number between 1 to 4! ")
        except ValueError:
            print(" ")
            print("You need to write a whole number...!")
                

c1 = False
a1 = int(0)
q1 = str("""Hello! Today we are going to take a little history quiz!

Who was the third president of the United States?

1. William Henry Harrison
2. Thomas Jefferson
3. John Quincy Adams
4. Martin Van Buren""")

run_quest(q1, a1, c1, 2)
    #print("You got...", score * 100, "%!")

##print(q1)
##while c1 == False:
##    try:
##        print(" ")
##        a1 = int(input("Please indicate your answer by selecting a number from 1-4.  "))
##        if a1 == 2:
##            score = score + 1
##            c1 = True
##        elif 0<a1<5:
##            c1 = True
##        else:
##            print(" ")
##            print("You can only choose a number between 1 to 4!")
##    except ValueError:
##        print(" ")
##        print("You need to write an actual number…!")
##        
##print(" ")
##print("Alright! Hmm...now let's see....")
##print(" ")
##print("You got...", score * 100, "%!")

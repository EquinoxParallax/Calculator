import math
############## Global Vars ###############
debug_on = False

###############Functions ##################
def debug_print(msg):
    if (debug_on):
        print (msg)
    else:
        pass
###################Multiplycation fuctions#######
def to_the_power():
    z=pfi("What number?")
    y=pfi("To the power of what?")
    print(math.pow(z, y))

def Multiply():
    x=pfi("Hello, \nDear human, \nPlease tell me two numbers you would like me to multiply.\n(P.S one now one later)")
    y=pfi("And another one?")
    y=int (y)
    print (int(x) * y)
def factorial():
    y=pfi("What number do you want the factorial of")
    print(math.factorial(y))
###################Division fuctions#############
def Remainder_fuction():
    e=pfi("What number would you like to divide")
    f=pfi("How many groupes would you like")
    print("There are " + str(e // f)+" groupe(s)")
    print("With " + str(e % f) + " remaining")
    
def percent_fuction():
    e=pfi("What number would you like to divide")
    f=pfi("How many groupes would you like")
    print(e/f)
##############Addition######################
def addition_fuction():
    a=pfi("Please tell me two numbers un would like me to add together.")
    b=pfi("And another")
    print (a + b)
##############substraction##################
def substraction_fuction():        
    c=pfi("Please tell me the number you will substract from ")
    d=pfi("And the amount you will substract")
    print(c-d)
##############Multiplication################
def multy_fuction():
    w=-1
    while w!=0:
        w=pfi("would you like to \n1:Multiply, \n2:____ to the power, \n3:factorial, \n0:or Go back?")
        if(int(w)==1):
            Multiply()
        elif(int(w)==2):
            to_the_power()
        elif(int(w)==3):
            factorial()
        elif (w==0):
            continue
#############Division######################
def division_fuction():
    x=-1
    while x!=0:
        x=pfi("would you like to \n1:Have a Percentage, \n2:Have a remainder \n0:or go Back?\n")
        if(int(x)==1):
         percent_fuction()
        elif(int(x)==2):
            Remainder_fuction()
        elif (x==0):
            continue
#############Prime number identifier##############
def prime_fuction():
    x=pfi("Give me a number")
    half = x//2
    debug_print ("Half: "+str(half))
    i = 2
    rtn=-1
    rtn2 = -1
    while i <= half and rtn < 0:
        debug_print (i)
        debug_print (x % i)
        if(x%i == 0):
            rtn = i
            rtn2 = int (x / i)
        i+=1
    if (rtn2 == -1):
        print ("This is a prime number")
    else:
        print("We found that " + str(rtn) + " is a factor of " + str(x) + " and " + str (rtn2) + " is the other factor")      
    print ("The End")
    print(":0")

#Prompt for  Integer (pfi)
#takes a string, which is prompted to the user, and captures their response as an integer.
#includes error handeling.
def pfi(string):
    while True:
        try:
            return int(input(string))
        except:
            print("please select again")
####################### MAIN ############
x=-1
while x!=0:
    debug_print (x)
    x=pfi("would you like to \n1:Add, \n2:substract, \n3:Multiply, \n4:Divide, \n5:Check if a number is prime, \n0:or Quit?\n")
    if(int(x)==1):
        addition_fuction()
    elif(int(x)==2):
        substraction_fuction()
    elif(int(x)==3):
        multy_fuction()
    elif(int(x)==4):
        division_fuction()
    elif(int(x)==5):
        prime_fuction()
    elif (x==0):
        continue
    else:
        print("Please type 0,1,2,3,4 or 5,")

print ("Thank you for using my program!")

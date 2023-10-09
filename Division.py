def pfi(string):

    while True:
        try:
            return int(input(string))
        except:
            print("please select again")
def Remainder_fuction():
    e=pfi("What number would you like to divide")
    f=pfi("How many groupes would you like")
    print("There are " + str(e // f)+" groupe(s)")
    print("With " + str(e % f) + " remaining")

def percent_fuction():
    e=pfi("What number would you like to divide")
    f=pfi("How many groupes would you like")
    print(e/f)
def division_fuction():
    x=-1
    while x!=0:
        x=pfi("would you like to \n1:Have a Percentage, \n2:Have a remainder \n0:or Quit?\n")
        if(int(x)==1):
         percent_fuction()
        elif(int(x)==2):
            Remainder_fuction()
    print ("Thank you for using my program!")







#e=pfi("What number would you like to divide")
#f=pfi("How many groupes would you like")
#print("There are " + str(e // f)+" groupe(s)")
#print("With " + str(e % f) + " remaining")

division_fuction()
percent_fuction()
Remainder_fuction

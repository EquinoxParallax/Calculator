#=================Addition==================
def pfi(string):
    while True:
        try:
            return int(input(string))
        except:
            print("please select again")
a=pfi("Please tell me two numbers un would like me to add together.")
b=pfi("And another")
print (a + b)

    

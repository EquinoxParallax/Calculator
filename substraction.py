def pfi(string):
    while True:
        try:
            return int(input(string))
        except:
            print("please select again")
            
def substraction_fuction():        
    c=pfi("Please tell me the number you will substract from ")
    d=pfi("And the amount you will substract")
    print(c-d)

substraction_fuction()

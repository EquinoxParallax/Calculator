x=int(input("Give me a number"))
half = x//2
print ("Half: "+str(half))
i = 2
rtn=-1
rtn2 = -1
while i <= half and rtn < 0:
    print (i)
    print (x % i)
    if(x%i == 0):
        rtn = i
        rtn2 = int (x / i)
    i+=1
if (rtn2 == -1):
    print ("This is a prime number")
else:
    print("We found that " + str(rtn) + " is a factor of " + str(x))
    print("and " + str (rtn2) + " is the other factor")      
print ("The End")
print(":0")



print("this is current bill program")
unit=int(input("enter the unit"))
if(unit<=100):
    print("the curent bill is zero")
elif(unit>100)and (unit<=200):
    bill=unit*2
    print("the current bill is : ",bill)
elif(unit>200)and (unit<=300):
    bill=unit*3.5
    print("the current bill is : ",bill)
elif(unit>300)and (unit<=400):
    bill=unit*5
    print("the current bill is : ",bill)
else:
    bill=unit*8
    print("the current bill is : ",bill)

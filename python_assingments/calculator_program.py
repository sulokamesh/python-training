print("this is calculator program")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter your choice"))
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
if(choice==1):
    ans=num1+num2
    print("sum of {num1} and {num2} is : {ans}".format(num1=num1,num2=num2,ans=ans))
elif(choice==2):     
    ans=num1-num2
    print("sub of {num1} and {num2} is : {ans}".format(num1=num1,num2=num2,ans=ans))
elif(choice==3):
    ans=num1*num2
    print("multiplication of {num1} and {num2} is : {ans}".format(num1=num1,num2=num2,ans=ans))
elif(choice==4):
    ans=num1//num2
    print("division of {num1} and {num2} is : {ans}".format(num1=num1,num2=num2,ans=ans))
else:
    print("enter the valied number")

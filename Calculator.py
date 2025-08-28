print("hello,how can help you today?")
print("Welcome to Calculator!") 
h=int(input("enter the first number"))
i=input("enter the operator:+,-,*,/,%)")
j=int(input("enter the second number"))
if i=="+":
   print("your addition is:",h+j)
elif i=="-":
   print("your subtraction is:",h-j)
elif i=="*":
   print("your multiplication is:",h*j)
elif i=="/":
   print("your division is:",h/j)
elif i=="%":
   print("your modules is:",h/j*100)
else:
    print("your wrong operator")
print("Thank you for using Calculator ")
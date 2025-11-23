n1=float(input("ENTER THE FIRST NUMBER"))
operator=input("ENTER THE OPERATOR")
n2=float(input("ENTER THE SECOND NUMBER"))
if operator=="+":
    print("SUM OF NUMBERS IS:",n1+n2)
elif operator=="-":
    print("DIFFERENCE OF THE NUMBERS IS:",n1-n2)
elif operator=="x":
    print("PRODUCT OF THE NUMBERS IS:",n1*n2)
elif operator=="/":
    print("QUOTIENT OBTAINED BY THE DIVISION IS:",round(n1/n2,4)) 

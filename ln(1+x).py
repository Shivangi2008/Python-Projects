#ln(1+x)
x=float(input("Enter value of x such that x blongs to(-1,1]"))
if x<=-1 or x>1:
    print("invalid input")
else:
    sum1=0
    n=999
    for i in range(1,n+1):
        sum1+= (x**i)*(-1)**(i-1)/i
    print("ln(1+x) is ", sum1)

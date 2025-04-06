print("To calculate e^x")
x=int(input(("Enter value of x")))
n=99
fact=1
sum=1
for num in range(1,n):
    fact *= num  # Factorial for current term
    sum += (x ** num) / fact  # Add the next term to the sum
print("e**x", sum)

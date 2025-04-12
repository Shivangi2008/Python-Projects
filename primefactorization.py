def prime_factors(n):
    factors = []
    
    # First, remove all the 2s (smallest prime)
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2

    # If n is still greater than 2, it's prime
    if n > 2:
        factors.append(n)
    
    return factors

# Get input from user
num = int(input("Enter a number to find its prime factors: "))

if num <= 1:
    print("Enter a number greater than 1.")
else:
    result = prime_factors(num)
    print(f"Prime factors of {num} are: {result}")

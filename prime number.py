

def is_prime(n):
    """Returns True if the number n is prime, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Prints all prime numbers between start and end (inclusive)."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

# Input: start and end
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end}:")
find_primes_in_range(start, end)


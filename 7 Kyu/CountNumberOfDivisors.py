# Given a number, return the number of divisiors
def divisors(n):
    return len([i for i in range(1,n+1) if not n % i])
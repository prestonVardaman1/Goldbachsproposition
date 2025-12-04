import math
#Disproving Goldbachs proposition
'''

Upon reading the prompt "Write a computer program to determine the smallest odd 
composite number that cannot be written as the sum of a prime and twice a square."

I determined there are 2 total CORE functions to successfully disprove Goldbachs proposition

1. check for prime numbers
    For this function I programmed check_prime to take integer n and check if its less than or equal to 1
    then if that statement is false, it will iterate through a for loop 2 <= (sqrt of n) +1
2. check for if a number is twice a perfect square
    checks odd and small values and checks possible squares

3. main iteration to brute force check
'''





def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):#we actually talked about this in class
        if n % i == 0:
            return False
    return True

#very unoptimized but for the purpose of this program its fine
def twice_squared(n):
    if n % 2 != 0:  # odd can't be twice a square
        return False
    if n < 2:  # less than 2 cant be twice a square
        return False

    for i in range(1, n + 1):
        if 2 * i * i == n:
            return True
        if 2 * i * i > n:
            break
    return False

def smallest_composite():
    n = 9  # smallest odd composite
    while True:
        print("Testing: " + str(n))
        if check_prime(n) == False:  # if composite
            found = False
            for p in range(2, n):
                if check_prime(p):
                    r = n - p
                    if twice_squared(r):
                        found = True
                        break
            if not found:
                return n
        n += 2  # next odd number


if __name__ == '__main__':
    print(smallest_composite())




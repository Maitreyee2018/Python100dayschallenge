#This program determines whether a number is prime or not

#prime checker function accept a number as parameter and prints whether it is prime or not
def prime_checker(number):
    not_prime=False
    for i in range(2,number):
        if number%i==0:
            not_prime=True

    if not_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


#Enter the number to determine prime or not prime
n = int(input("Check this number: "))
prime_checker(number=n)

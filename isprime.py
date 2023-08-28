def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            print("The Number is not Prime")
            return
    else:
        print("The Number is Prime")
print("Hello")
num = int(input("Enter a Number : "))
isprime(num)

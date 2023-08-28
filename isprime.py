def isprime(_num):
    for i in range(2, _num):
        if _num % i == 0:
            print("The Number is not Prime")
            return
    else:
        print("The Number is Prime")


print("Hello")
_num = int(input("Enter a Number : "))
isprime(_num)

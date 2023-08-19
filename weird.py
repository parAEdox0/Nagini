#Input number is odd = Weird
#Input number is even between 2 to 5 = Not Weird
#Input number is even between 6 to 20 = Weird
#Input number is evern between 20 to 100 = Not Weird
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and 20 < n:
    print("Not Weird")

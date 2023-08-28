marks = []
present = []
absent = []
num = int(input("ENTER NUMBER OF STUDENTS : "))
print()
print("(ENTER MARKS OBTAINED OUT OF 20 OR 'ab' IF ABSENT)")

for i in range(1, num+1):
    val = input(f"ENTER MARKS OBTAINED BY ROLL NUMBER {i} : ")
    if val == "ab" or 0 <= int(val) <= 20:
        marks.append(val)
    else:
        print("YOU'VE ENTERED WRONG INPUT PLEASE ENTER MARKS OUT OF 20 OR 'ab' IF ABSENT")
        exit(1)
k = 1
for j in marks:
    if j == "ab":       
        absent.append(k)
        k = k + 1
    else:
        present.append(j)
print()
print("THE NUMBER OF PRESENT STUDENTS = ", len(present))
print("THE NUMBER OF ABSENT STUDENTS = ", len(absent))
print()


def avg():
    sum_m = 0
    for m in range(0, len(present)):
        sum_m = int(sum_m) + int(present[m])
    print("THE AVERAGE MARKS OF THE STUDENTS ARE = ", float(sum_m / len(present)))


def high():
    _high = 0
    for n in range(0, len(present)):
        if int(_high) < int(present[n]):
            _high = present[n]
    print("THE HIGHEST MARKS OF THE CLASS = ", _high)


def low():
    _low = 10
    for n in range(0, len(present)):
        if int(_low) > int(present[n]):
            _low = present[n]
    print("THE LOWEST MARKS OF THE CLASS = ", _low)


avg()
high()
low()

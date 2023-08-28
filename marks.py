marks = []
present = []
absent = []
num = int(input("ENTER NUMBER OF STUDENTS : "))
print()

for i in range(1, num+1):
    val = input(f"ENTER MARKS OBTAINED BY ROLL NUMBER {i} : ")
    marks.append(val)
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

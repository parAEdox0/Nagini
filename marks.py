marks = []
present = []
absent = []
num = int(input("ENTER NUMBER OF STUDENTS : "))

for i in range(1, num+1):
    val = input(f"ENTER MARKS OBTAINED BY ROLL NUMBER {i} : ")
    marks.append(val)
    # print(marks)
k = 1
for j in marks:
    if j == "ab":       
        absent.append(k)
        k = k + 1
    else:
        present.append(j)

print("The Number of Present students = ", len(present))
print("The Number of Absent students = ", len(absent))

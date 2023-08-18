percentage = float(input("Enter percentage % : "))

if percentage >= 95:
    grade = "A+"
elif percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
elif percentage >= 40:
    grade = "P"
else:
    grade = "F"

print("You got Grade:", grade, "📚")

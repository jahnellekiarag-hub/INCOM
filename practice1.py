Kiara_classrecord = {
    "Liza": {
        "StudID": "5001",
        "Grade": [90, 85, 86, 82, 83, 90, 92]
    },
    "Jeremy": {
        "StudID": "5002",
        "Grade": [90, 75, 59, 80, 84, 75, 85]
    }
}

student = input("Enter student name: ")

if student in Kiara_classrecord:
    print("\nStudent found!")
    print("")
    grades = Kiara_classrecord[student]["Grade"]
    print("Grades:", grades)


    average = sum(grades) / len(grades)
    print("Average:", round(average, 2))


    if any(grade < 60 for grade in grades):
        print("Candidate for intervention")


    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))

else:
    print("\nStudent not found.")
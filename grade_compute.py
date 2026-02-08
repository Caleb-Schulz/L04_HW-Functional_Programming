def verify(grades_list):
    valid_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    for grade in grades_list:
        if grade=="Q":
            print("Exiting Program. ")
            exit()
        if grade in valid_grades:
            pass
        else:
            print(f"Invalid input: '{grade}' is not a recognized grade.")
            exit()

def top_3(grades_list):
    top_3_grades = grades_list[:]
    dropped_grade = top_3_grades.pop(0)
    return top_3_grades, dropped_grade

def grade_to_number(grades):
    grade_letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade_values  = [4.0, 3.7,  3.3,  3.0, 2.7,  2.3,  2.0, 1.7,  1.3,  1.0, 0.0]
    grades_values = []
    for grade in grades:
        idx = grade_letters.index(grade)
        grades_values.append(grade_values[idx])
    return grades_values

def number_to_grade(grades):
    grade_letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade_values  = [4.0, 3.7,  3.3,  3.0, 2.7,  2.3,  2.0, 1.7,  1.3,  1.0, 0.0]
    grades_letters = []
    for grade in grades:
        for i in range(len(grade_values)):
            if grade >= grade_values[i]:
                grades_letters.append(grade_letters[i])
                break
    return grades_letters

def average(top_3_grades):
    top_grades_values = grade_to_number(top_3_grades)
    add=0
    for grade in top_grades_values:
        add += grade
    average_grade = add/3
    return round(average_grade, 2)

def final(average_grade):
    if average_grade <= 2.7:
        curved_grade = average_grade +0.25
        grade = [curved_grade]
    else:
        grade = [average_grade]
    final_letter = number_to_grade(grade)
    return final_letter[0]

def summary(grades_list, dropped, average, final_letter):
    entered = ", ".join(grades_list)
    print("-" * 40)
    print(f"|{'GRADE REPORT SUMMARY':^38}|")
    print("-" * 40)
    print(f"| Grades Entered: {entered:<22}|")
    print(f"| Lowest Grade Dropped: {dropped:<16}|")
    print(f"| Calculated Average: {average:<18}|")
    print(f"| Final Letter Grade: {final_letter:<18}|")
    print("-" * 40)

    return grades_list


def sorting(grades_list):
    grades_list = grade_to_number(grades_list)
    grades_list.sort()
    grades_list = number_to_grade(grades_list)
    return grades_list
        
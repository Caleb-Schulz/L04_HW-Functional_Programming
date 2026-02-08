import grade_compute as gc

def main():
    grades_input=input("Enter 4 letter grades with a $ between each or Q to quit.\n").upper()
    grades_list = grades_input.split("$")
    gc.verify(grades_list)
    grades_list = gc.sorting(grades_list)
    top_3_grades, dropped_grade = gc.top_3(grades_list)
    average_grade = gc.average(top_3_grades)
    final_letter = gc.final(average_grade)

    gc.summary(grades_list, dropped_grade, average_grade, final_letter)


main()
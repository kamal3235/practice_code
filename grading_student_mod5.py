


def grading_student(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5

            if mod5 >= 3:
                grade += (5 - mod5)
                print(grade)
        res.append(grade)
    return res

print(grading_student([73, 67, 38, 33]))
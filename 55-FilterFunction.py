#Filter function
"""
-The function must return a Boolean iterable
-Like map, filter returns a generator, so we need to use the list function.

        filter(func, iterable)

"""

#Usage
def pass_grade_normal (list_grades):
    pass_grade_list = []
    for current_grade in list_grades:
        if current_grade >50:
            pass_grade_list.append(current_grade)
    return pass_grade_list

list_grade = [60, 55, 100, 20, 35, 59]
print(pass_grade_normal(list_grade)) #only the grades above 50 are printed

#using another way
def pass_grade_filter(grade):
    return grade > 50

grade = 60
print(grade>50)

#using only 2 lines of code we created the got the same output as the using the normal function
passed_grade_filter = list(filter(pass_grade_filter, list_grade))
print(passed_grade_filter)

#using the lambda function also gives the same output
passed_grade_filter_lambda = list(filter(lambda  grade: grade >50, list_grade))
print(passed_grade_filter_lambda)



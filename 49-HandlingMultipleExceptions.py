#Handling Multiple Exceptions
"""
-We can get many exceptions.
-Just like in conditional statements, the first exception is the only one that will be executed, and the other will be ignored.
-We can have a try except and else. Just like the if condition, you can add an else clause while handling errors.
-There is also the finally clause. The finally clause runs whether the try statement produces an exception or not.
=If a finally clause is present, the finally clause will execute as the last task before the try statement completes.
-If the exception is not handled by an exception clause, the exception is re-raised after the finally clause has been executed.
-If the try statement reaches a break, continue or return statement, the finally clause wil execute just prior to the break,
continue or return statement's execution.
-If a finally clause includes a reutrn statement, the returned value will be the one from the finally clause's return statement,
not the value from the try clause's return statement.
"""

#Usage
def divide(x, y):
    try:
        result = x/y
        assert x>=y
    except ZeroDivisionError:
        result = "Cannot divide by 0"
    except AssertionError:
        print("Error. x is less than y")
    return result

print(divide(6,3))
print(divide(4,8))
print(divide(3,0))
print("hello")

"""
========================================
📘 PYTHON VARIABLES – THEORY + CODE
========================================

WHAT IS A VARIABLE?
-------------------
A variable is a name given to a memory location.
It is used to store data values in a program.

In Python:
- No need to declare data type explicitly
- Python is dynamically typed
"""

# -------------------------------
# 1. VARIABLE DECLARATION
# -------------------------------
x = 10
name = "Python"
price = 99.99

print(x)
print(name)
print(price)


"""
HOW VARIABLES WORK IN PYTHON
----------------------------
Python decides the data type at runtime.
The same variable can store different types.
"""

# -------------------------------
# 2. DYNAMIC TYPING
# -------------------------------
x = 10
print(x, type(x))

x = "Hello"
print(x, type(x))

x = 5.5
print(x, type(x))


"""
RULES FOR NAMING VARIABLES
--------------------------
1. Must start with a letter or underscore (_)
2. Cannot start with a number
3. Can contain letters, numbers, underscores
4. Case-sensitive
5. Cannot use Python keywords
"""

# -------------------------------
# 3. VALID VARIABLE NAMES
# -------------------------------
age = 21
_name = "Sushma"
total_marks = 500

print(age, _name, total_marks)

# ❌ INVALID (DO NOT RUN)
# 1name = "error"
# class = 10


"""
MULTIPLE VARIABLE ASSIGNMENT
----------------------------
Python allows assigning multiple values in one line.
"""

# -------------------------------
# 4. MULTIPLE ASSIGNMENT
# -------------------------------
a, b, c = 10, 20, 30
print(a, b, c)

x = y = z = 100
print(x, y, z)


"""
VARIABLE SCOPE
--------------
Scope defines where a variable can be accessed.
"""

# -------------------------------
# 5. GLOBAL VARIABLE
# -------------------------------
g = 50

def show_global():
    print("Global variable:", g)

show_global()


# -------------------------------
# 6. LOCAL VARIABLE
# -------------------------------
def show_local():
    l = 10
    print("Local variable:", l)

show_local()


"""
CHECKING VARIABLE TYPE
----------------------
Use type() function to know data type.
"""

# -------------------------------
# 7. TYPE CHECKING
# -------------------------------
x = 100
print(type(x))


"""
DELETING A VARIABLE
-------------------
Use del keyword to remove a variable.
"""

# -------------------------------
# 8. DELETE VARIABLE
# -------------------------------
temp = 999
print(temp)
del temp
# print(temp)  # NameError if uncommented


"""
BEST PRACTICES
--------------
- Use meaningful variable names
- Follow snake_case
- Avoid single-letter names
"""

# -------------------------------
# 9. BEST PRACTICE EXAMPLE
# -------------------------------
student_name = "Sushma"
total_score = 480

print(student_name)
print(total_score)





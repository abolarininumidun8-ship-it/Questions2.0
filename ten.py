
# 1. print("A variable is a name refers to a value stored in a memory.")

#  2. age = 25
# name = "Alice"
# print("Name:", name)
# print("Age:", age)

# 3.print("A variable name cannot start with a number.")

# 4.age = 25
# print("Age:", age)

# 5. name = "Kelechi"
# print("Name:", name)

# 6. x = 5
# y = x
# print ("Q6:", y)

# 7. Using type() determines the class type of a variable.

# 8.print("= is used to assign a value to a variable.")
# print("== is used to compare two values to see if they are equal.")

# 9. print("you can change a variable's value simply by reassigning it using the = operator, or by modifying mutable objects in place.")

# 10.print("Variable assignment is the process of giving a value to a variable, allowing it to store and later reference that value in a program.")

# 11. a, b, c = 1, 2, 3
# print(f"a = {a}, b = {b}, c = {c}")

# 12. a, b = 10, 20
# print(a, b)

# 13. Swap without a third variable
a, b = 5, 10
a, b = b, a
print("Q13:", a, b)  # 10 5



# 14. print("Variables in Python start with a letter or underscore.")
# print("Variables can contain letters, numbers, and underscores, but cannot start with a number.")
# print("Variables cannot be a python key word")

# 15. print("my_var")

# 16. print("No,Name and name are the same thing.") 

# 17. print("A constant is a value whose value is intended and remain unchanged throughout the program.")
PI_EXAMPLE = 3.14159  # convention only, still technically changeable


# 18.
import math
print(math.pi) # PI = 3.14

# 19.
x = 10
x = 20
print("Q19:", x)  # 20

# 20.print("a variable can be deleted using the del keyword")
# x = "Hello World"
# del x
# print(x) # This will raise a NameError because x has been deleted.

# 21.
school = "Noun"

# 22.
is_student = True
print("is_student:", is_student)

# 23. Q23 in the doc has a typo ("name _ 2"); correct example:
name = "Attah"
print("Q23:", name * 2)  # AttahAttah

# 24.print(second_name) # This will print "Maxwell" without any error.
second_name = "Maxwell"

# 25. Fix: 'class' is a reserved keyword
class_name = "Python"

# 26. id() it returns the identifier associated with an object.
x = 10
print(id(x))  # This will print the unique identifier for the integer object 10.

#27. None means no value
x = None

# 28.
x = y = z = "Python"
print("Q28:", x, y, z)

# 29. Dynamic typing = a variable's type is decided at runtime and can change.
val = 5
val = "now a string"
print("Q29:", val)

# 30.
price = 100
price += 50
print("Q30:", price)  # 150

# 31. snake_case: words separated by underscores, e.g. my_variable_name

# 32. camelCase: first word lowercase, next words capitalized, e.g. myVariableName

# 33. Python's standard for variables is snake_case (PEP 8).

# 34. NameError: name 'x' is not defined

# 35.
full_name = "Bella Sterling"
my_age = 20
state = "Lagos"

a = 10; b = 20; a = b; 
print("Q36:", a)  # 20


x = "5"; y = "10"
print("Q37:", x + y)  # "510" (string concatenation)

x=5; y=10; 
print("Q38:", x + y)  # 15

a=True; print("Q39:", type(a))  # <class 'bool'>

num = 10
num = num + 5
print("Q40:", num)  # 15

a=5; a+=3; print("Q41:", a)  # 8

a=10; b=a; b=20; 
print("Q42:", a)  # 10 (b was a copy of the value, not linked)

# 43. x, y = 5  -> ValueError: cannot unpack non-iterable int object
#     (unpacking needs an iterable with 2 items, e.g. x, y = 5, 6)

first_name = "John"; last_name = "Doe"
print("Q44:", first_name + last_name)   # JohnDoe
print("Q45:", first_name + " " + last_name)  # John Doe

print("=== CHALLENGE ===")

# 46. print("input() function is used to take input from the user and return it as a string.")
 
# 47. name = input("Hello, What's your name?")

# 48. print("local variable is a variable that is defined within a function and can only be accessed within that function while a global variable is defined outside of any function and can be accessed from anywhere in the program.")

# 49.
counter = 0
def increment():
    global counter
    counter += 1
increment()
print("Q49:", counter)  # 1

# 50. print("A del keyword is used to delete a variable from memory.")
my_list = [1, 2, 3, 4, 5]
del my_list[2] # Deletes the third item
print("Q50:",my_list)

# 51. Yes, functions are objects and can be assigned to variables.
x = print
x("Q51: this was called through variable x")

# 52. print('Variable shadowing occurs when a variable declared within a certain scope (like a function) has the same name as a variable declared in an outer scope. The inner variable "shadows" the outer one, making the outer variable inaccessible within that inner scope.')
value = "global"
def shadow_demo():
    value = "local"  # shadows the global 'value' inside this function
    return value
print("Q52:", shadow_demo(), "|", value)

sentence = "I'm a student "
print("Q53:", sentence)

# 54. Python has no built-in immutable variables, but naming convention

# 55.print("A _ variable is a name that refers to a value stored in memory. It can be used to store data, such as numbers, strings, or objects, and can be changed or updated throughout the program.")

x=10; y=20; x,y = y,x
print("Q56:", x, y)  # 20 10

a = 100

def my_function():
    a = 200
    print("Q57 Inside function, a =", a)

my_function()

print("Outside function, a =", a)

# 58. print("Python keywords cannot be used as variable names because they are reserved words with predefined meanings in the language. ")

# 59.
print("Q59:", ["if", "else", "for", "while", "def"])


# 60. print("type() returns the exact type of an object, while isinstance() checks if an object is an instance of a class or its subclasses.")
#     isinstance() checks if an object IS an instance of a type (or subclass) -> True/False.
print("Q60:", type(5) == int, isinstance(5, int))

# 61. 
my_list = ["Bella", "Bob", "Bethel"]
print("Q61:", my_list)

# 62.
data = {
    "name": "Max",
    "age": 20
}
print("Q62:", data)

# 63. 
x = y = z = 0
print("Q63:", x, y, z)

## 64. Unpacking = assigning items of an iterable to multiple variables.
#     (Note: [1][2][3] in the doc is a typo; correct form below)
a, b, c = [1, 2, 3]
print("Q64:", a, b, c)


# 65
a = [1][2]   
b = a        
b.append(3)  
print("Q65:", a)  # [1, 2, 3]

# 66.print("copy of variable a is created and assigned to variable b. When we append 3 to b, it also affects a because they both refer to the same list object in memory.")

# 67. print("A variable is a reference to an object in memory,not a direct storage of the object's value")


68. 
x = 42
name = "Alice"
numbers = [1, 2, 3]



# show_defined_variables()

#  69. print("x is None checks object identity, while x == None checks for equality.") 

# phone number is a string
phone_number = "07065723423"
print("70:", phone_number)


print("Q71:", "strings")
print("booleen")
print("float")
print("integer")

# 72. print("integer,float,decimal")

# 73. print("int are whole numbers")
# print("float are decimal numbers")

# 74. print("Strings are sequences of characters written in quotes.")

# 75. print("A boolean is a data type that can have one of two values: True or False.")

value = 10.5
print("Q76:",value, "is of type:", type(value))

# 77. value = 10
# print(value, "is of type:", type(value))

# 78. value = 'a'
# print(type(value))

# 79. result = (10 > 9) 
# print(result)

# 80. print("lists")

# 81. value = (1,2,3)
# print(value, "is of type:", type(value))

# 82. data = {1, 2, 3}
# print(type(data))

# 83. print(type({"a": 1}))

# 84. print(type(None))
  
# 85. 
x = 10
y = 3.14
z = "Hello"

print("Q85:", type(x)) 
print(type(y)) 
print(type(z))

# 86.
num = 10
num_str = str(num)

print(num_str)       
print("Q86:", type(num_str))

s = "10"
num = int(s)
print("Q87:", num)

# 88. int("hello") #This will raise a valueError because "hello" cannot be converted to an integer.

# 89.
num_float = 10.5
num_int = int(num_float)
print("Q89:", num_int)

# 90.
print("Q90:", bool (0))

print("Q91:", bool (1))

empty_str = ""
result = bool(empty_str)
print("Q92:", bool(empty_str))

print("Q93:", str(100) + str (200))

print("Q94:", int(10.5))

# Define a list
my_list = ["apple", "cherry", "banana"]
# convert it using tuples
my_tuple = tuple(my_list)

print("Q95:", "converted tuple:", my_tuple)
print("data type:", type(my_tuple))

# 96.
# using double quotes ""
# using single quotes ''
# using triple quotes """ """

# 97.
# using double quotes "" means if the string  contain  an apostrophe or single quotes
# using single quotes '' means if the string contains double quotes

# 98.
# using the triple quotes
text = """ This is line one
this is line two
This line three"""
print("Q98:", repr(text))

print("Q99:", len("python")) # Output = 6

print("Q99:", len("Python"))       # 6
s = "Python"
print("Q100:", s[0])              
print("Q101:", s[0:3])             
print("Q102:", s[-1])              
print("Q103:", "python".upper())   
print("Q104:", "PYTHON".lower())   
print("Q105:", "Hello" + " " + "World") 

print("Q106:", "Hi" * 3)          
name_, age_ = "Max", 20
print("Q107 f-string:", f"My name is {name_} and I am {age_}")
print("Q108:", f"My name is {name_} and I am {age_}")

print("Q109 strip:", "  hello  ".strip())  # "hello"
print("Q110:", "python" in "I love python")  # True


# 111
# list is an array of a value assigned to a variable using the square bracket[] and is mutable
# 112
# tuple is a built-in data type used to store a collection of items in a single variable() and is immutable.

# 113
# list is mutable because it can add , remove or change element after the list is created while
# tuple is immutable you can't add or remove element after the tuple is created

# 114
# dict is a built-in data type used to store data in a key value pairs {} and is mutable.

# 115.
# set is a built-in data type used to store a collection of unique items and is mutable.   
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print("Q115:", fruits)

# 118.
# mutuable means  to add, remove or change e.g set, dict
# immutable means permanent e.g tuple

a = [1,2];
a[0] = 99;
print("Q119:", a)

print("Q120:", type([]))
print("Q121:", type(()))
print("Q122:", type({})) #  Output = dict


my_empty_set = set()
print("Q123:", type(my_empty_set))

my_dict = {}
print("Q124:", type(my_dict)) 

print("Q125:", type([]) , type({}))

print("Q126:", type([]), type({}))

# 127. Indexing = accessing an item in a sequence by its position, e.g. s[0]

print("Q128:", len([1,2,3,4]))

print("Q129:", bool([]), bool([0]))

print("Q130:", bool(""), bool(" ")) 

x = 5
print("Q131:", isinstance(x, int))  # True

# 132. complex numbers have a real and imaginary part
c = 3 + 5j
print("Q132:", c, type(c))

# 133. A list can hold values of MANY different data types at once (unlimited mix).

my_list_dup = [1, 2, 2, 3]
print("Q134:", set(my_list_dup))  # {1, 2, 3} -- duplicates removed

# 135. NoneType is the type of the special value None.
print("Q135:", type(None))

# 136. '==' compares VALUES for equality; 'is' compares IDENTITY (same object in memory).

# 137.
# user_input = input("Enter something: ")
# print(type(user_input))   # always <class 'str'>, input() always returns a string

int_v, float_v, str_v, bool_v = 1, 1.0, "a", True
list_v, tuple_v, dict_v, set_v = [1], (1,), {"a": 1}, {1}
print("Q138:", int_v, float_v, str_v, bool_v, list_v, tuple_v, dict_v, set_v)

print("Q139:", type(True), issubclass(bool, int))

# 140. Floats are stored in binary, and 0.1 and 0.2 can't be represented
#      exactly in binary, causing tiny rounding errors.
print("Q140:", 0.1 + 0.2, 0.1 + 0.2 == 0.3) 

# 141. 7 arithmetic operators: +, -, *, /, //, %, **
print("Q142 (+):", 5 + 3)

print("Q143 (-):", 5 - 3)

print("Q144 (*):", 5 * 3)          
print("Q145 (/):", 10 / 3, "-> always returns a float")
print("Q146 (//):", 10 // 3, "-> floor division, drops the remainder")
print("Q147 (%):", 10 % 3, "-> remainder/modulo")
print("Q148 (*):", 2 * 3)
print("Q149:", 10 / 3) 
print("Q150:", 10 // 3) 
print("Q151:", 10 % 3) 

# 152. Operator precedence = the order operations are evaluated (like math: * and / before + and -)
print("Q152:", 2 + 3 * 4)   # 14, not 20 (multiplication happens first)

print("Q153:", 2 * 3 * 2, "-> left to right: (2*3)*2 = 12")

length, width = 10, 5
print("Q154 area:", length * width)  # 50

principal, rate, time = 1000, 5, 2
simple_interest = (principal * rate * time) / 100
print("Q155 simple interest:", simple_interest)  # 100.0

# 156. 6 comparison operators: ==, !=, >, <, >=, <=
print("Q157 (==):", 5 == 5)
print("Q158 (!=):", 5 != 3)
print("Q159 (> <):", 5 > 3, 3 < 5)
print("Q160 (>= <=):", 5 >= 5, 5 <= 5)
print("Q161:", 5 == 5.0)   
print("Q162:", "5" == 5)   
print("Q163:", 10 > 5)     
print("Q164:", True == 1) 
print("Q165:", False == 0) 
 
# 166. and -> True if BOTH are true; or -> True if AT LEAST ONE is true; not -> flips the boolean
print("Q167:", True and False)  # False
print("Q168:", True or False)   # True
print("Q169:", not True)        # False
print("Q170:", 5 > 3 and 10 > 5)  # True
print("Q171:", 5 > 10 or 10 > 5)  # True

# 172. 5 assignment operators: =, +=, -=, *=, /=
val = 10
val += 5; print("Q173 (+=):", val)
val -= 3; print("Q174 (-=):", val)
val *= 2; print("Q175 (*=):", val)   

# 177. x += 1 is the same as x = x + 1
# 178. '=' assigns a fresh value; '+=' adds to the existing value and reassigns.

print("Q179 (in):", "a" in "apple")        # True
print("Q180 (not in):", "z" not in "apple")  # True

list1 = [1, 2]
list2 = [1, 2]
print("Q181 (is):", list1 is list1)   # True, same object
print("Q182:", "'==' compares VALUES, 'is' compares IDENTITY (memory location)")

a_ = [1, 2]
b_ = [1, 2]
print("Q183:", a_ == b_, a_ is b_) 

print("Q184:", "a" in "apple")             # True
print("Q185:", 3 in [1, 2, 3])             # True
print("Q186:", "key" in {"key": 1})        # True

# 187. 'in' on a dict checks the KEYS by default, not the values.
print("Q187 check:", "key" in {"key": 1}, 1 in {"key": 1})  # True, False

print("Q188 (& |):", 5 & 3, 5 | 3)  # bitwise AND=1, OR=7

# 189. Ternary operator: value_if_true if condition else value_if_false
x_ = 10
a_ternary = "big" if x_ > 5 else "small"
print("Q189:", a_ternary)

n = 7
print("Q190:", "even" if n % 2 == 0 else "odd")

# 191. Operator chaining lets you combine comparisons: 1 < 2 < 3 means (1<2) and (2<3)
print("Q191:", 1 < 2 < 3)  # True

print("Q192:", 10 + 20 * 30 / 10)  # 10 + (20*30/10) = 10 + 60 = 70.0

# 193. Use () to force a different order of evaluation
print("Q193:", (10 + 20) * 30 / 10)  # (30)*30/10 = 90.0

print("=== CHALLENGE (small programs) ===")

# 194.
n1, n2 = 10, 3
print("Q194:", n1 + n2, n1 - n2, n1 * n2, n1 / n2, n1 % n2, n1 // n2)

# 195.
age_check = 20
print("Q195:", age_check >= 18)

# 196.
number = 15
print("Q196:", number % 3 == 0 and number % 5 == 0)

# 197.
letter = "e"
print("Q197:", letter in "aeiou")

# 198.
num_double = 2
for _ in range(3):
    num_double *= 2
print("Q198:", num_double)  # 16

# 199. BODMAS = Brackets, Orders(powers), Division/Multiplication, Addition/Subtraction.
#      Python follows this same order of operations.

# 200. Small calculator
def calculator(a, b):
    return {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else "undefined",
        "%": a % b if b != 0 else "undefined",
        "//": a // b if b != 0 else "undefined",
    }

print("Q200:", calculator(10, 3))

# 201.
# user_name = input("Enter your name: ")
# print(user_name.upper())
user_name = "bella"  # simulated input for demo
print("Q201:", user_name.upper())

# 202. NameError: name 'x' is not defined (del removes the variable entirely)
x = 10
del x
try:
    print(x)
except NameError as e:
    print("Q202: NameError ->", e)

# 203.
a, b = 10, "10"
try:
    a + b
except TypeError as e:
    print("Q203: TypeError ->", e, "(can't add int + str directly, types must match)")

# 204.
a, b = "Python", "Java"
a, b = b, a
print("Q204:", a, b)  # Java Python

# 205.
a, b, c = 5, 10, 15
print("Q205:", a + b + c)  # 30

# 206.
x = 50
print("Q206:", id(x))

# 207.
first, last = "Attah", "Maxwell"
full_name = f"{first} {last}"
print("Q207:", full_name)

# 208. Valid identifiers: __name, _age, age_, age2 are all valid.
#      2age is INVALID (can't start with a digit).
print("Q208 valid:", ["__name", "_age", "age_", "age2"])

# 209.
x = 5
x = x + x   # 10
x = x + x   # 20
print("Q209:", x)  # 20

# 210.
count = 0
while count < 10:
    count += 1
print("Q210:", count)  # 10

# 211. Python uses dynamic typing: the interpreter infers a variable's type
#      from the value assigned to it at runtime, so no declaration is needed.

# 212.
data = [1, 2, 3]
data2 = data          # data2 points to the SAME list object as data
data2[0] = 99
print("Q212:", data)  # [99, 2, 3] -- data changed too, because both names reference one list

# 213. Fix with .copy() to create an independent list
data = [1, 2, 3]
data2 = data.copy()
data2[0] = 99
print("Q213:", data, data2)  # [1, 2, 3] [99, 2, 3]

# 214.
student1, student2, student3 = "Ada", "Ben", "Chi"
print("Q214:", [student1, student2, student3])

# 215. globals() returns a dict of all variables in the global scope.
#      locals() returns a dict of all variables in the current local scope.
print("Q215 sample locals():", list(locals().keys())[-3:])

# 216.
student_maths_score_2024 = 85

# 217. Yes, this is valid — it's a conditional expression used as a statement.
x_, y_ = 10, 20
print(x_, y_) if x_ > y_ else print(y_, x_)  # prints "20 10"

# 218.
a, b = 10, 20
result = a if a > b else b
print("Q218:", result)  # 20

# 219. No. Python 3 identifiers must be letters, digits, or underscores
#      (Unicode letters are allowed, but emoji are NOT valid identifier characters).
try:
    exec("😀 = 10")
except SyntaxError as e:
    print("Q219: SyntaxError ->", e)

# 220. '_' is used to ignore/discard a value during unpacking.
a, _b, c, _, _ = [1, 2, 3, 4, 5]
print("Q220:", a, _b, c)  # 1 2 3

# 221.
price, qty = 19.99, 3
total = price * qty
print("Q221:", total)  # 59.97

# 222.
# name = input("Enter name: ")
# age = int(input("Enter age: "))   # convert to int for numeric use
name, age = "Ada", int("20")
print("Q222:", name, age, type(age))

# 223. Both give the same result here; int(10) is redundant since 10 is
#      already an int. int() is only useful for converting OTHER types.
print("Q223:", 10 == int(10))

# 224.
is_logged_in = False
is_logged_in = not is_logged_in
print("Q224:", is_logged_in)  # True

# 225.
a = None
print("Q225:", a is None)  # True

# 226.
x_outer = 10
def my_func():
    x_inner = 5
    print("Q226 (inside func):", x_inner)
my_func()
print("Q226 (outside func):", x_outer)

# 227. Convention: write the name in ALL_CAPS (e.g. MAX_SIZE = 100) to signal
#      "treat this as constant" — Python won't enforce it, but other devs will respect it.

# 228.
text = "NOUN"
length = len(text)
print("Q228:", length)  # 4

# 229.
name = "bella"
name = name + " Noun"
print("Q229:", name)  # Kelechi Noun

# 230. Error because \n and \f are interpreted as escape sequences
#      (newline, form-feed) instead of literal backslashes.
#      Fix using a raw string with an 'r' prefix:
file_path = r"C:\new\folder"
print("Q230:", file_path)

print("\n=== DATA TYPES - LOGIC & BUG FINDING (231-270) ===")

print("Q231:", type(1 / 2), "-> float, because '/' ALWAYS returns a float in Python 3")
print("Q232:", type(2 // 2), "-> int, because '//' (floor division) returns an int when both inputs are int")

# 233. No. "True" is a string (4 characters); True is a boolean value. They differ in type.
print("Q233:", "True" == True, type("True"), type(True))

print("Q234:", int(True), int(False))  # 1 0

print("Q235:", str(True) + str(False))  # "TrueFalse"

# 236. bool("False") is True because ANY non-empty string is truthy,
#      regardless of its content/text.
print("Q236:", bool("False"))  # True

# 237. Two ways to check for an empty string:
s_check = ""
print("Q237:", s_check == "", len(s_check) == 0)

s = " python is easy "
s = s.strip().upper().replace("EASY", "POWERFUL")
print("Q238:", s)

try:
    "python"[100]
except IndexError as e:
    print("Q239: IndexError ->", e)

print("Q240:", "python"[1:100], "-> no error, slicing beyond the end just stops at the last character")

# 241. Strings are immutable — individual characters cannot be reassigned.
try:
    s_immut = "python"
    s_immut[0] = "P"
except TypeError as e:
    print("Q241: TypeError ->", e)

s_rev = "python"
print("Q242:", s_rev[::-1])  # reverse using slicing

print("Q243:", len(" "), len(""))  # 1 0

age_str = "20"
age_num = int(age_str) + 5
print("Q244:", age_num)  # 25

print("Q245:", list("abc"), "vs", ["abc"], "-> list('abc') splits into characters; [\"abc\"] is a single-item list")

print("Q246:", [1, 2, 3] * 2)   # [1, 2, 3, 1, 2, 3]  (doc's '_' = '*')
print("Q247:", (1, 2, 3) * 2)   # (1, 2, 3, 1, 2, 3)

try:
    {"a": 1} * 2
except TypeError as e:
    print("Q248: TypeError ->", e, "(dicts don't support repetition)")

# 249. Dict keys must be hashable (immutable). Lists are NOT hashable -> error.
#      Tuples ARE hashable (if their contents are), so they CAN be dict keys.
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print("Q249a: list as key -> TypeError:", e)
good_dict = {(1, 2): "value"}
print("Q249b: tuple as key ->", good_dict)

print("Q250:", set([1, 1, 2, 2, 3]))  # {1, 2, 3}

# 251. Sets use .add(); 252. Lists use .append()
set_demo = {1, 2}
set_demo.add(3)
list_demo = [1, 2]
list_demo.append(3)
print("Q251/252:", set_demo, list_demo)

# 253. Common mistake: naming a variable 'list' shadows the built-in list().
#      [1,2,3].append(4) works fine on the literal, but it's a throwaway
#      (not stored), and reusing the name 'list' for a variable is bad practice.
temp_list = [1, 2, 3]
temp_list.append(4)
print("Q253:", temp_list)

a_ = [1, 2]
b_ = a_
b_ = [3, 4]          # this REBINDS b_ to a new list, doesn't touch a_
print("Q254:", a_)   # [1, 2] -- unchanged, since b_ now points elsewhere

t = (1, 2, 3)
t_list = list(t)
t_list.append(4)
t = tuple(t_list)
print("Q255:", t)  # (1, 2, 3, 4)

d = {"name": "Max", "dept": "NOUN"}
print("Q256 keys:", list(d.keys()))
print("Q256 values:", list(d.values()))

# 257. Both work, but isinstance() is preferred: it also accounts for
#      subclasses (e.g. isinstance(True, int) is True), making it more robust.
print("Q257:", isinstance([1, 2], list), type([1, 2]) == list)

# 258. None is used to represent "no value yet" or "missing/optional result",
#      e.g. a function that returns nothing, or a default parameter placeholder.
def find_user(uid):
    return None  # user not found
print("Q258:", find_user(1))

print("Q259:", float("inf"), type(float("inf")))  # inf <class 'float'>

print("Q260:", int(True) + int(False) + int(True))  # 1+0+1 = 2

x_check = 10.5
print("Q261:", "float" if isinstance(x_check, float) else "int" if isinstance(x_check, int) else "other")

# 262. Shallow copy: copies the outer object, but nested objects are still
#      shared references (list.copy(), copy.copy()).
#      Deep copy: recursively copies everything, no shared references
#      (copy.deepcopy()) — use it when the object contains nested mutable objects.
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)
shallow[0].append(99)  # affects nested too, since inner lists are shared
print("Q262:", nested, deep)

a_ch = "5"
b_ch = int(a_ch)
c_ch = float(b_ch)
print("Q263:", c_ch)  # 5.0

mixed_list = [1, "two", 3.0, True, None]
print("Q264:", mixed_list)

# 265. bool([0]) is True because the list [0] is NON-EMPTY (it has 1 item).
#      Truthiness of a list depends on whether it has items, not their values.
print("Q265:", bool([0]))  # True

# 266. bytes: an immutable sequence of raw bytes, e.g. b"hello".
#      bytearray: a MUTABLE version of bytes, can be modified in place.
print("Q266:", bytes([104, 105]), bytearray([104, 105]))

print("Q267:", str(123), float("123"))  # "123"  123.0

x_nested = ["a", "b", "c"]  # doc's ["a"]["b"]["c"] is a typo (nested indexing doesn't apply to flat strings)
print("Q268:", x_nested[0])  # 'a'  (["a"]["b"]["c"] as literally written would error: str has no index "b")

print("Q269:", complex(2, 3))  # (2+3j)

# 270.
def detect_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        return "string"
print("Q270:", detect_type("42"), detect_type("hello"))

print("\n=== OPERATORS - CALCULATION & LOGIC (271-300) ===")

print("Q271:", 2 * 3 * 2, "-> (2*3)=6, then 6*2=12")

print("Q272:", -3 * 2, "-> -6, not -9 (a negative times a positive stays negative)")
# Note: the doc's numbers imply a typo; -3 * 3 = -9 is likely intended:
print("Q272b:", -3 * 3, "-> -9 (negative * positive = negative)")

print("Q273:", (-3) ** 2, "-> 9 (negative squared becomes positive; doc's '__' = '**')")

print("Q274:", 10 + 3 * 2 * 2, "-> BODMAS: multiply first (3*2*2=12), then add 10 -> 22")

weight, height = 70, 1.75
bmi = weight / (height ** 2)
print("Q275 BMI:", round(bmi, 2))

x = 15
print("Q276:", 10 < x < 20)  # True, chained comparison

print("Q277:", 5 == 5 and 10 == 10 and 15 == 20)  # False (last condition fails)
print("Q278:", 5 == 5 or 10 == 20 or 15 == 20)     # True (first condition passes)
print("Q279:", not (5 > 3))  # False

print("Q280:", not 0, not 1, not "")  # True False True

# 281. Short-circuit: 'and' stops at the first False, so 10/0 is NEVER evaluated -> no error
print("Q281:", False and (10 / 0 if False else "skipped"))
result_281 = False and False  # simulating: real 10/0 never runs due to short-circuit
print("Q281 (real):", result_281)

# 282. 'or' stops at the first True, so 10/0 is never evaluated -> no error
print("Q282:", True or False)

print("Q283 (10):", 10 % 2 == 0 and 10 % 3 == 0)  # False (10 not divisible by 3)
print("Q283 (15):", 15 % 2 == 0 and 15 % 3 == 0)  # False (15 not divisible by 2)

# 286. doc's '2_3' is likely a typo for 2*3
a286 = 5
a286 += 2 * 3
print("Q286:", a286)  # 11

x287 = 10
x287 //= 3
print("Q287:", x287)  # 3

x288 = 2
x288 *= 3
x288 *= 2
print("Q288:", x288)  # 12

# 289. Functionally identical result; += is shorter and, for mutable objects
#      like lists, can modify in place rather than creating a new object.
print("Q289:", "same result, += is just shorthand for x = x + 1")

print("Q290:", "ab" in "abc" and "d" not in "abc")  # True

def check_letter(letter, word="python"):
    return letter in word
print("Q291:", check_letter("y"), check_letter("z"))

# 292. Small integers (-5 to 256) are cached/interned by Python, so `a is b`
#      is True for a=b=1000... actually 1000 is OUTSIDE that cache range,
#      so behavior can vary; small numbers like 10 ARE cached -> True.
a292, b292 = 1000, 1000
print("Q292 (1000):", a292 is b292,
      "-> result is implementation-dependent (CPython may or may not reuse the object;"
      " 1000 is outside the guaranteed small-int cache of -5 to 256)")
a292b, b292b = 10, 10
print("Q292 (10):", a292b is b292b, "-> True, small ints ARE cached/reused by Python")

print("Q293:", [] == [], [] is [])  # True False (equal values, different objects)

v1, v2, v3 = 5, 5, 5
print("Q294:", v1 == v2 and v2 == v3)  # True

# 295. Walrus operator ':=' assigns a value AND returns it in the same expression.
my_list_295 = [1, 2, 3]
if (n := len(my_list_295)) > 2:
    print("Q295: list has", n, "items")

# 296.
# while (cmd := input("Type something (or 'exit'): ")) != "exit":
#     print("You typed:", cmd)
print("Q296: (interactive loop shown as comment above; needs real input())")

print("Q297:", 10 & 2, "-> bitwise AND compares bits: 1010 & 0010 = 0010 = 2")
print("Q298:", 10 | 2, "-> bitwise OR: 1010 | 0010 = 1010 = 10")

# 299. Swap using XOR (only works reliably for integers)
p, q = 5, 9
p = p ^ q
q = p ^ q
p = p ^ q
print("Q299:", p, q)  # 9 5

# 300. Final mini calculator
def mini_calculator(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2 if n2 != 0 else "undefined"
    elif op == "%":
        return n1 % n2 if n2 != 0 else "undefined"
    elif op == "//":
        return n1 // n2 if n2 != 0 else "undefined"
    elif op == "**":
        return n1 ** n2
    else:
        return "invalid operator"

print("Q300:", mini_calculator(10, 3, "+"))
print("Q300:", mini_calculator(10, 3, "**"))

# 301. Yes, Python is dynamically typed (a variable can point to any type,
#      and can be reassigned to a different type). It is also STRONGLY typed
#      (it won't silently convert between incompatible types, e.g. "5"+5 errors).
x = 5
print("Q301:", x)
x = "hello"
print("Q301:", x)

# 302. Bug: input() always returns a STRING, so age + 10 tries to add int to str -> TypeError.
# Fix:
name = "Ada"          # simulated input
age = "20"            # simulated input
age = int(age)        # convert to int before doing math
print("Q302:", age + 10)

# 303. Because Python doesn't pre-declare variables; if the `if` branch never
#      runs, `x` is never created, so referencing it raises NameError.
if False:
    x_never = 10
try:
    print(x_never)
except NameError as e:
    print("Q303: NameError ->", e)

# 304.
name = "Ada Obi"
matric_no = "NOU/2024/001"
course = "Computer Science"
gpa = 4.5
is_active = True
print("Q304:", name, matric_no, course, gpa, is_active)

# 305. Surprise: all three point to the SAME list object, so appending
#      through c affects a and b too.
a = b = c = [1]
c.append(2)
print("Q305:", a, b, c)  # [1, 2] [1, 2] [1, 2]

# 306. Avoid by creating independent objects instead of chaining mutable ones:
a2, b2, c2 = [1], [1], [1]
c2.append(2)
print("Q306:", a2, b2, c2)  # [1] [1] [1, 2]

# 307. NameError: using a variable that was never defined.
#      TypeError: using an operation on the wrong type (e.g. "1"+1).
#      ValueError: right type but invalid value (e.g. int("abc")).

# 308.
try:
    print(undefined_variable)  # crashes on purpose
except NameError as e:
    print("Q308: NameError ->", e)
undefined_variable = 5  # fix: define it first
print("Q308 fixed:", undefined_variable)

# 309.
g_x = 10
def show_x():
    x_local = 20  # a DIFFERENT variable, local to this function
    print("Q309 (inside func):", x_local)
show_x()
print("Q309 (global):", g_x)

# 310.
x_glob = 10
def change_global():
    global x_glob
    x_glob = 20
change_global()
print("Q310:", x_glob)  # 20

# 311. nonlocal lets an inner (nested) function modify a variable from its
#      ENCLOSING function's scope (not global, not fully local).
def outer():
    val = 1
    def inner():
        nonlocal val
        val = 2
    inner()
    return val
print("Q311:", outer())  # 2

# 312. Yes, you can chain assignments. It's fine for immutable values (numbers,
#      strings), but risky for mutable objects (lists/dicts) since all names
#      share the SAME object (see Q305).
a3 = b3 = c3 = 10
print("Q312:", a3, b3, c3)

# 313. '_' is the conventional name for a throwaway variable you don't intend to use.
for _ in range(5):
    pass
print("Q313: looped 5 times using throwaway variable _")

# 314.
first_name, last_name = "Attah", "Maxwell"
full_name_1 = first_name + " " + last_name
full_name_2 = " ".join([first_name, last_name])
full_name_3 = f"{first_name} {last_name}"
print("Q314:", full_name_1, "|", full_name_2, "|", full_name_3)

# 315.
sentence = "I love Python"
word_count = 0
current_word = False
for ch in sentence:
    if ch != " " and not current_word:
        word_count += 1
        current_word = True
    elif ch == " ":
        current_word = False
print("Q315:", word_count)  # 3

# 316.
x316 = 10
y316 = "10"
print("Q316:", x316 is int(y316))  # True here -- 10 is a small int (-5 to 256),
                                     # so CPython reuses the same cached object;
                                     # for larger numbers this would likely be False

# 317.
# name = input("Name: "); age = int(input("Age: ")); phone = input("Phone: ")
# Phone is kept as a STRING because it may start with 0 and is never used in math.
name317, age317, phone317 = "Ada", 20, "08012345678"
print("Q317:", name317, age317, phone317)

# 318. PI = 3.14 can still be reassigned because Python has no true "const"
#      keyword. ALL_CAPS is only a NAMING CONVENTION that signals intent to
#      other developers -- it is not enforced by the language.
PI = 3.14
PI = 3.14159  # still works, Python won't stop you
print("Q318:", PI)

# 319. Small integers (-5 to 256) are cached by CPython, so a and b point to
#      the SAME cached object -> same id.
a319, b319 = 5, 5
print("Q319:", id(a319) == id(b319))  # True

# 320. 257 is outside the guaranteed small-int cache range. In a script,
#      Python may still fold identical literals in the same code block
#      (True); in the interactive IDLE shell, each line is compiled
#      separately, so it's often False. Behavior is implementation detail.
a320, b320 = 257, 257
print("Q320:", a320 is b320, "(implementation-dependent; don't rely on 'is' for value comparison)")

# 321.
p, q, r = 1, 2, 3
del p, q, r
print("Q321: p, q, r deleted")

# 322. Use dir() (names only) or globals() (name->value dict) to list variables.
sample_var = 1
print("Q322 sample:", [n for n in dir() if not n.startswith("_")][:5])

# 323. Shadowing a built-in: naming a variable 'str' hides the built-in str() function.
str_backup = str  # save the real builtin first (safety, not required by the question)
str = "hello"
try:
    print(str(10))
except TypeError as e:
    print("Q323: TypeError ->", e, "(str is now a string, not the built-in function anymore)")
str = str_backup  # restore it

# 324. Dangerous because any later code in that scope that expects str() to be
#      the built-in function will crash unexpectedly -- hard-to-find bugs.

# 325.
x325 = [1, 2, 3]
y_ref = x325          # SAME object as x325
y_copy = x325.copy()  # INDEPENDENT copy
y_ref.append(4)
print("Q325 reference:", x325)   # changed: [1, 2, 3, 4]
y_copy.append(99)
print("Q325 copy:", x325)        # unaffected: [1, 2, 3, 4]

# 326.
balance = 1000
for _ in range(3):
    balance -= 100
print("Q326:", balance)  # 700

# 327. Dynamic variable creation via globals() dict manipulation:
globals()['x' + str(1)] = 10
print("Q327:", x1)  # 10

# 328. Avoid dynamic variable names: they make code hard to read, hard to
#      debug, and break tools like linters/autocomplete. Use a dict instead,
#      e.g. data = {"x1": 10}.

# 329.
a329, b329, c329 = 1, 2, 3
a329, b329, c329 = b329, c329, a329
print("Q329:", a329, b329, c329)  # 2 3 1

# 330. True behaves like 1 in arithmetic (bool is a subclass of int).
x330 = True
x330 = x330 + 5
print("Q330:", x330)  # 6

# 331.
data = None
if data is None:
    print("Q331: data has not been assigned yet")
data = 5
if data is not None:
    print("Q331: data is now assigned:", data)

# 332.
num1, num2 = 15, 4
total_sum = num1 + num2
difference = num1 - num2
product = num1 * num2
print("Q332:", total_sum, difference, product)

# 333. Stack: fast, small memory for function calls and simple local variable
#      references. Heap: larger memory pool where actual objects (lists,
#      dicts, custom objects) live; variables on the stack just hold
#      references pointing into the heap. (Simplified: Python manages this
#      automatically, unlike C.)

# 334.
name334 = " noun "
clean_name = name334.strip().capitalize()
print("Q334:", repr(clean_name))  # 'Noun'

# 335.
my_name = "ADA"
letters = [ch for ch in my_name]  # one variable per letter, via list here
joined = "".join(letters)
print("Q335:", letters, "->", joined)

"""
SECTION E2: DATA TYPES - DEEP DIVE (336-390) - Answered
Run: python section_e2_datatypes.py
"""

import sys
import copy
import json
import math

print("=== 336-390 ===")

print("Q336:", type([]), type(()), type({}), type(set()))

# 337. {} is always an empty DICT (dict literal syntax came first in Python's
#      design). To make an empty SET you must use set().
print("Q337:", type({}), "-> use set() for an empty set:", set())

print("Q338:", bool(0), bool(0.0), bool(0j), bool(""), bool([]), bool({}), bool(None))
# All False

# 339. 7 falsy values: False, None, 0, 0.0, "", [], {} (also (), set(), 0j)
print("Q339:", [False, None, 0, 0.0, "", [], {}])

# 340. Surprising truthy values: "False" (non-empty string), " " (space string),
#      [0] (non-empty list, even though it holds a falsy item)
print("Q340:", bool("False"), bool(" "), bool([0]))

print("Q341:", repr("hello" * 0), repr("hello" * -5))
# "" for both -- 0 or negative repeat count gives an empty string

lst_mult = [1, 2]
try:
    lst_mult * 2.5
except TypeError as e:
    print("Q342: TypeError ->", e, "(can only multiply a list by an int)")

print("Q343:", "Python"[::-1], "-> reverses the string using a step of -1")

s344 = "Python Programming"
print("Q344:", s344[:3], s344[-3:])  # 'Pyt' 'ing'

print("Q345:", ord('A'), chr(65))  # 65 A

def is_palindrome(text):
    return text == text[::-1]
print("Q346:", is_palindrome("madam"), is_palindrome("hello"))

print("Q347:", repr("  hi  ".strip()), repr("  hi  ".lstrip()), repr("  hi  ".rstrip()))

print("Q348 split:", "a,b,c".split(","))
print("Q348 join:", "-".join("a,b,c".split(",")))

sentence349 = "I love Java"
sentence349 = sentence349.replace("Java", "Python")
print("Q349:", sentence349)

s350 = "hello"
id_before = id(s350)
s350 += "!"
id_after = id(s350)
print("Q350:", id_before == id_after, "-> False, strings are immutable so += creates a NEW string object")

# 351. append([4,5]) adds the LIST ITSELF as one single element.
#      extend([4,5]) adds each ELEMENT of the list individually.
a351 = [1, 2, 3]
a351.append([4, 5])
print("Q351 append:", a351)  # [1, 2, 3, [4, 5]]
b351 = [1, 2, 3]
b351.extend([4, 5])
print("Q351 extend:", b351)  # [1, 2, 3, 4, 5]

# 352. append() modifies the list IN PLACE and returns None (no new value to return).
a352 = [1, 2, 3]
result_352 = a352.append(4)
print("Q352:", result_352, "->", a352)  # None -> [1, 2, 3, 4]

# 353. Insert at the beginning with insert(0, item)
a353 = [2, 3]
a353.insert(0, 1)
print("Q353:", a353)

# 354. remove(value) deletes the FIRST matching value; pop(index) deletes by
#      position (and returns the removed item); pop() with no index removes the last.
a354 = [1, 2, 3, 2]
a354.remove(2)   # removes first '2'
print("Q354 remove:", a354)
popped = a354.pop(0)  # removes item at index 0
print("Q354 pop:", popped, a354)

a355 = [1, 2, 3]
a355.pop()     # removes last item (3)
a355.pop(0)    # removes first item (1)
print("Q355:", a355)  # [2]

# 356. Yes -- the tuple itself is immutable (you can't replace its elements),
#      but if an element is a MUTABLE object (like a list), that object can
#      still be changed in place.
t356 = ([1, 2], 3)
t356[0].append(99)
print("Q356/357:", t356, "-> no error, because we mutated the LIST inside, not the tuple itself")

# 358. No, (5) is just an int in parentheses, NOT a tuple.
print("Q358:", type((5)))  # <class 'int'>

# 359. Add a trailing comma to make it a real single-element tuple
single_tuple = (5,)
print("Q359:", type(single_tuple), single_tuple)

# 360. Sets can only hold HASHABLE (immutable) items. Lists are unhashable -> error.
#      Tuples are hashable, so they CAN go inside a set.
try:
    bad_set = {[1, 2]}
except TypeError as e:
    print("Q360a: TypeError ->", e)
good_set = {(1, 2)}
print("Q360b:", good_set)

# 361. Hashable = has a fixed hash value that never changes during its lifetime
#      (required for dict keys / set members). Lists are mutable, so their
#      contents (and thus hash) could change -- Python disallows this to
#      prevent broken lookups.

# 362. Yes. True == 1 and False == 0 in Python, so they collide as dict keys.
d362 = {True: "yes", 1: "no", 1.0: "maybe"}
print("Q362:", d362, "-> only ONE key remains (True/1/1.0 are all treated as equal keys)")

d363 = {"a": 1}
try:
    d363["b"]
except KeyError as e:
    print("Q363 direct access: KeyError ->", e)
print("Q363 .get():", d363.get("b"))          # None, no error
print("Q363 .get(default):", d363.get("b", 0))  # 0

d1, d2 = {"a": 1}, {"b": 2}
merged = d1 | d2   # Python 3.9+ merge operator
print("Q364:", merged)

d365 = {"a": 1, "b": 2}
print("Q365:", type(d365.keys()), type(d365.values()), type(d365.items()))
# dict_keys, dict_values, dict_items (view objects, not lists)

nums_str = "123,456,789"
nums_int = [int(n) for n in nums_str.split(",")]
print("Q366:", nums_int)

nums_list = [1, 2, 3]
joined_str = "-".join(str(n) for n in nums_list)
print("Q367:", joined_str)

mapped = list(map(int, ["1", "2", "3"]))
print("Q368:", mapped, type(mapped))  # [1, 2, 3] <class 'list'>

mixed369 = [1, "a", 2.5, True, None, [1]]
for item in mixed369:
    print("Q369:", item, "->", type(item).__name__)

print("Q370:", isinstance(True, int), "-> True, because bool is defined as a SUBCLASS of int in Python")

# 371. isinstance() correctly accounts for subclasses/inheritance;
#      type() == checks the EXACT type only. isinstance() is generally preferred.
class MyInt(int):
    pass
mi = MyInt(5)
print("Q371:", isinstance(mi, int), type(mi) == int)  # True False

def convert_if_digit(value):
    return int(value) if value.isdigit() else value
print("Q372:", convert_if_digit("42"), convert_if_digit("abc"))

data373 = {"students": [{"name": "Max", "scores": [90, 80]}]}
print("Q373:", data373["students"][0]["scores"][1])  # 80

nested374 = [[1, 2], [3, 4]]
shallow374 = nested374.copy()
deep374 = copy.deepcopy(nested374)
shallow374[0].append(99)   # affects nested374 (shared inner list)
print("Q374:", nested374, deep374)

a375 = float("nan")
print("Q375:", a375 == a375, "-> False, NaN is defined to never equal anything, even itself")

print("Q376:", math.isnan(float("nan")), "-> use math.isnan() to check for NaN")

# 377. None = absence of a value; 0 = the number zero; "" = empty string;
#      False = boolean false. They are all FALSY but NOT the same as each other or equal via 'is'.
print("Q377:", None == 0, 0 == "", "" == False, "-> all False, they are different types/values")

lst378 = [1, 1, 2, 2, 3, 3]
no_dup_set = list(set(lst378))
print("Q378:", no_dup_set, "-> order is NOT guaranteed with a plain set")

no_dup_ordered = list(dict.fromkeys(lst378))
print("Q379:", no_dup_ordered, "-> dict.fromkeys() preserves insertion order (Python 3.7+)")

print("Q380:", len([[]]), len([]))  # 1 0 -- [[]] has ONE item (an empty list)

print("Q381:", b"hello", type(b"hello"), "-> byte strings represent raw binary data, used in file I/O, networking, encoding")

sentence382 = "I have 5 apples and 3.5 kg of rice"
counts = {"int": 0, "float": 0, "string": 0}
for word in sentence382.split():
    if word.replace(".", "", 1).isdigit():
        if "." in word:
            counts["float"] += 1
        else:
            counts["int"] += 1
    else:
        counts["string"] += 1
print("Q382:", counts)

print("Q383:", sys.getsizeof(10), sys.getsizeof("hello"), sys.getsizeof([1, 2, 3]))

x384 = 10
print("Q384: type=", type(x384), "id=", id(x384), "value=", x384, "size=", sys.getsizeof(x384))

def check_mutability(value):
    try:
        value[0] = value[0]  # attempt an in-place item change
        return "mutable"
    except (TypeError, IndexError):
        return "immutable"
print("Q385:", check_mutability([1, 2]), check_mutability((1, 2)))

a386 = "python"
print("Q386:", a386 is "python", "-> works here due to string interning, but 'is' should NOT be used for string comparison; use =='")

# 387. String interning: Python may reuse the SAME memory object for identical
#      short strings/simple literals to save memory -- an implementation detail, not a guarantee.

student388 = {
    "name": "Ada",
    "age": 20,
    "courses": ["Math", "Physics"],
    "grades": {"Math": "A", "Physics": "B"}
}
print("Q388:", student388)

student_json = json.dumps(student388)  # module: json
print("Q389:", student_json)

def data_type_report(value):
    print("Q390 value:", value)
    print("Q390 type:", type(value))
    print("Q390 id:", id(value))
    print("Q390 bool:", bool(value))
    print("Q390 mutable:", check_mutability(value) if isinstance(value, (list, tuple)) else "n/a")
data_type_report([1, 2, 3])



# 391. BODMAS: 5 + (2*3) * (2/2) - 1  =>  5 + 6*1 - 1 = 5 + 6 - 1 = 10
print("Q391:", 5 + 2 * 3 * 2 / 2 - 1)  # 10.0

print("Q392:", 100 / 10 / 2, "-> evaluated LEFT to right: (100/10)/2 = 10/2 = 5.0")
print("Q393:", 100 // 10 // 2, "-> (100//10)//2 = 10//2 = 5")

print("Q394:", 2 * 3 * 2, (2 * 3) * 2, "-> identical: 12 12 (multiplication is left-associative anyway)")

principal, rate, years = 1000, 5, 2
compound_interest = principal * (1 + rate / 100) ** years - principal
print("Q395:", round(compound_interest, 2))

print("Q396:", -10 / 3, -10 // 3, "-> '/' gives -3.333..., '// ' floors DOWN (towards negative infinity) to -4, not -3")

print("Q397:", 10 % -3, -10 % 3, "-> Python's % result always takes the SIGN of the divisor, unlike some other languages")

print("Q398:", divmod(10, 3), "-> (quotient, remainder), same as (10//3, 10%3)")

n399 = 1234
digits = []
temp = n399
while temp > 0:
    digits.insert(0, temp % 10)
    temp //= 10
print("Q399:", digits)

# 400. Floats are stored in binary, and most decimal fractions (like 0.1)
#      cannot be represented exactly in binary -> tiny rounding errors occur.
print("Q400:", 0.1 + 0.2 == 0.3, 0.1 + 0.2)

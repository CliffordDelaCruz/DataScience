#002.01.functions.py
#function is a rule for taking zero or more inputs and returning a corresponding output

def double(x):
    return x * 2

#python functions are first-class, means we can assign them to variables and pass them into functions just like any other arguments
def apply_to_one(f):
    return f(1)

my_double = double              #refers to the previously defined function
x = apply_to_one(my_double)     # equals 2

#it is easy to create short anonymous functions or lambdas
y = apply_to_one(lambda x: x + 4)   # equals 5

#Function parameters can also be given default arguments, which only need to be specified when you want a value other thatn the default
def my_print(message = "my default message"):
    print(message)

my_print("hello!")  #prints 'hello'
my_print()          #prints 'my default message'
import operator

num1 = float(input("Enter the first number:"))
op = input("Input the operator:")
num2 = float(input("Enter the second number:"))
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow
}
result_num = 0
Val_op = True


def calculate():
    global result_num
    if op in ops:
        op_func = ops[op]
        result = op_func(num1, num2)
        print(result)
        result_num = result
    else:
        print("Invalid operator")
        Val_op = False


def calculate_again():
    global result_num
    op = input("Input the operator:")
    num3 = float(input("Input a number:"))
    if op in ops:
        op_func = ops[op]
        result = op_func(result_num, num3)
        print(result)
        result_num = result
    else:
        print("Invalid operator")
        Val_op = False


calculate()

while not(Val_op):
    calculate_again()

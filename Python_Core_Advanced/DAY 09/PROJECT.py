# in this calculator we are using different function learning how function work.

def num1():
    a= float(input("Enter the first number: "))
    return a

def num2():
    b= float(input("Enter the second number: "))
    return b

def operator(a):
    operation_dict = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    for i in operation_dict:
        print(i)
    x=input("Enter the operation: ")

    return operation_dict[x](a, num2())


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


def command_choosed(choice,previous_result):
    if choice == "y":
        new_input = num2()
        final_answer=operator(previous_result,new_input)
        print(final_answer)
        future_choice_option(final_answer)

    elif choice == "n":
        main()
    else:
        exit()

def future_choice_option(answer):
    command = input(f"TYPE Y to continue to add with {answer} , TYPE n to start new calculation, 'Exit' to close the calculator.").lower()
    (command_choosed(command,answer))

def main():
    answer = operator(num1())
    print(f"The Calculated value is {answer}")
    future_choice_option(answer)



if __name__ == "__main__":
    main()

try:
    x=float(input("Enter First Number: "))
    y=float(input("Enter Second Number: "))
    print("what do you want to Do")
    print("Press and Enter\n+ for addition \n- for Subtraction \n* for Multiplication \n/ for Division \n'%' for reminder")
    option=input()
    match(option):
        case "+":
            print(f"{x} + {y} = {x+y}")
        case "-":
            print(f"{x} - {y} = {x-y}")
        case "*":
           print(f"{x} * {y} = {x*y}")
        case "/":
            print(f"{x} / {y} = {x/y}")
        case "%":
            print(f"{x} % {y} = {x%y}")
except Exception as e:
    print(f"Something is wrong with the {e} \n Please enter valid values")
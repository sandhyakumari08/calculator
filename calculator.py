try:
    a=int(input("Enter First Number: "))
    b=int(input("Enyer Second Number: "))

    print("Choose arithmetic operator to perform: \n",
          "Add\n",
          "Subtract\n",
          "Multiply\n",
          "Divide\n")
    
    arithmetic_operation=input().strip().lower()

    if arithmetic_operation=="add":
        total=a+b
    elif arithmetic_operation=="subtract":
        total=a-b
    elif arithmetic_operation=="multiply":
        total=a*b
    elif arithmetic_operation=="divide":
        if b==0:
            print("Error! can't divide by zero. ")
        else:
            total=a/b
    else:
        print("Invalid Operation! ")
    if total is not None:
        print(f"The Result is: {total}.")
except ValueError:
    print("Invalid Input! Please Enter Valid Numbers!")

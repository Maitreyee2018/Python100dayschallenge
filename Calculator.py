#Calculator program
from replit import clear
new_calculation=True

operation_options="'+'\n'-'\n'*'\n'/'"

def calculator(num1,num2,operation):
  if operation =="+":
    return num1+num2
  elif operation =="-":
    return num1-num2  
  elif operation =="*":
    return num1*num2  
  elif operation =="/":
    return num1/num2
  

while new_calculation:
  num1=float(input("What is the first number?: "))
  existing_calculation=True
  while existing_calculation:
    print(operation_options)
    operation=input("Pick an operation: ")
    num2=float(input("What's the second number?: "))
    result=calculator(num1,num2,operation)  
    print(f"{num1} {operation} {num2} = {result}")
    decide=input(f"Type 'y' to continue calculating with        {result}, or type 'n' to start a new calculation: ")

    if decide=='y':
      num1=result
    else:
      existing_calculation=False
      clear()
    




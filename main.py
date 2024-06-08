operation = input("Do you want to add, minus, multiply, or divide? ")

if operation == "add":
  firstNumber = input("What is the first number? ")
  secondNumber = input("What is the second number? ")
  answer = int(firstNumber) + int(secondNumber)
  print(answer)
  
if operation == "minus":
  firstNumber = input("What is the first number? ")
  secondNumber = input("What is the second number? ")
  answer = int(firstNumber) - int(secondNumber)
  print(answer)
  
if operation == "multiply":
  firstNumber = input("What is the first number? ")
  secondNumber = input("What is the second number? ")
  answer = int(firstNumber) * int(secondNumber)
  print(answer)
  
if operation == "divide":
  firstNumber = input("What is the first number? ")
  secondNumber = input("What is the second number? ")
  answer = int(firstNumber) / int(secondNumber)
  print(answer)

# print("really simple Python calculator made by notkoln on github\ntype 'quit' to exit and type 'help' for a list of inputs\n\n")

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

while True:
  inp = input("calc> ")
  if inp == "quit":
    break
  elif inp == "help":
    print("add, subtract, multiply, divide, quit, help\n")
  elif inp == "add":
    n1, n2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(str(n1) + " + " + str(n2) + " = " + str(add(n1, n2)))
  elif inp == "subtract":
    n1, n2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(str(n1) + " - " + str(n2) + " = " + str(subtract(n1, n2)))
  elif inp == "multiply":
    n1, n2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(str(n1) + " * " + str(n2) + " = " + str(multiply(n1, n2)))
  elif inp == "divide":
    n1, n2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(str(n1) + " / " + str(n2) + " = " + str(divide(n1, n2)))
  else:
    print("Please enter something valid.")

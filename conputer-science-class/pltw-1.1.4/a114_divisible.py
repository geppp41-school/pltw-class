#   a114_divisible.py

# get two numbers from user
numbers = [int(input("number 1: ")), int(input("number 2: "))]

# loop while the numbers are not divisible (the remainder is not 0)
while numbers[0] % numbers[1] != 0 and numbers[1] % numbers[0] != 0:
    
  # inform user of result 
    print("deviding numbers resualts in a remander")
    print(str(numbers[0]) + " / " + str(numbers[1]) + " = " + str(numbers[0]/numbers[1]))
    print(str(numbers[1]) + " / " + str(numbers[0]) + " = " + str(numbers[1]/numbers[0]))
  # gather user input again
    numbers = [int(input("number 1: ")), int(input("number 2: "))]

# inform user of result 
print("numbers can be devided :)")
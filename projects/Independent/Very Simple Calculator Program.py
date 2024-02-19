#Very Simple Program

#Giving the User theri options on the calculator             
print(" 1. Add")
print(" 2. Subtract")
print(" 3. Multiply")
print(" 4. Divide")
print(" 5. Exponent")
print(" 6. Quit")
option = int(input("Choose an Option: "))
       
while(option != 6):
        #Option = Add
        if(option == 1):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            add  = num1+num2
            print(num1, "+", num2, "=", add)
            option = int(input("Choose an Option: "))
        #Option = Subtract          
        elif(option == 2):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            subtract = num1 - num2
            print(num1, "-", num2, "=", subtract)
            option = int(input("Choose an Option: "))
        #Option = Multiply
        elif(option == 3):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            multiply = num1 * num2
            print(num1, "*", num2, "=", multiply)
            option = int(input("Choose an Option: "))
        ##Option = Divide
        elif(option == 4):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            divide = num1 / num2
            print(num1, "/", num2, "=", divide)
            option = int(input("Choose an Option: "))
        #Option = Exponent
        elif(option == 5):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            expo = num1**num2
            print(num1, "^", num2, "=", expo)
            option = int(input("Choose an Option: "))
        #If user input isn't on the option's list
        elif(option != 1 or 2 or 3 or 4 or 5):
            print("Invalid")
            option = int(input("Choose an Option between 1 and 6: "))            
if(option == 6):
    print("Calculator Session Terminated")

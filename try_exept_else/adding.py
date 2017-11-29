# -*- coding: utf-8 -*-

while True:
    print("Calculator +, for quit press q")
    try:
        num1 = input("please give me first number : ")
        if num1 == 'q':
            break
        else:
            num1 = int(num1)

        num2 = input("please give me second number : ")
        if num2 == 'q':
            break
        else:
            num2 = int(num2)

    except ValueError or TypeError:
        print("You have to type only digits")
    else:
        print(int(num1) + int(num2))

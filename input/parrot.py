# -*- coding: utf-8 -*-

message = input("Tell me something, and I will repeat it back to you: ")
message = str(message)
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = int(input("how old are you").title())

print(age)
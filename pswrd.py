import random

// all the tyes, we'll use in generation
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()_-=[]}{'.,?><"

all = lower + upper + upper + symbol + number + lower + number + symbol

length = int(input("desired length of your password:"))

password = "".join(random.sample(all,length))
print("The Password generated for you is :- ",password)
(input)

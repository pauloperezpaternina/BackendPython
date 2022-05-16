# 3.1. Please find another value of the variable ccNumber that starts with the number 5 and makes this a successful test?
# ccNumber = "5XXXXX"
ccNumber = input('Enter any value: ')
if ccNumber[:1] == "5":
    print(True)
else:
    print(False)
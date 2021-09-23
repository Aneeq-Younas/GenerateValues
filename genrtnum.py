
while True:
    try:
        num= int(input("Enter a number: \n "))
        print(" Finally, You successfully entered: \n  ", num)
        break
    except ValueError:
        print(" Its not a number, Please enter a number. and try again..... \n ")

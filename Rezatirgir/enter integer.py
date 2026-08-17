count = 0
summ = 0

while True:
    inp = input('enter an integer number : ')
    if inp.isdigit():
        count = count + 1
        summ = summ + int(float(inp))
    elif ((inp.lower() == 'q' or inp.lower() == 'quit') and count == 0):
        print("you have entered nothing or what you have entered are not integer number ")
        break
    elif ((inp.lower() == 'q' or inp.lower() == 'quit' and count != 0)):
        print("the mean of number you have entered is : {}")









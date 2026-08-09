# Hop_Fizz Game

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("HopWiz")

    elif i % 3 == 0:
        print("Hop")

    elif i % 5 == 0:
        print("Wiz")

    else:
        print(i)
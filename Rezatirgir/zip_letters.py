

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_even = str[0:26:2]
str_odd = str[1:26:2]
number_odd = range(1,27,2)
number_even = range(2,27,2)
for odd_char , even_char , odd_num , even_numb  in zip(str_even,str_odd,number_odd,number_even):
    print("{0}_{1} , {2}_{3}".format(odd_num,odd_char,even_numb,even_char))
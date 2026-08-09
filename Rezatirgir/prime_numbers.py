SUMM = 0
count = 0
for i in range(1,1001):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2 :
        count = count + 1
        SUMM =SUMM+i
        print(i)
else:
    print (" {0} ta adad aval darim ke sum of them is {1}".format(count,sum))





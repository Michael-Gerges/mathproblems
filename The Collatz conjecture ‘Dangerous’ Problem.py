# how many steps does it take each number to reach 1 if you divide by 2 if even and multiply aby three and add one if odd


def thefunction(n):
    #print(int(n))
    if n %2 == 0:
        return n/2
    else:
        return n*3 + 1


for i in range(1,100):
    ans = thefunction(i)
    numberofsteps = 1
    while int(ans) != 1:
        ans = thefunction(ans)
        numberofsteps += 1
    #print(1)
    print("for number ", i,"number of steps is : ",numberofsteps )

    #print("new number: ", i)

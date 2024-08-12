def first_num(num1, num2):
    if num1>num2:
        raise ValueError ("num2 should be bigger rhen num1")
    for i in range(num1, num2+1):
        if (i%2 != 0):
            print (i)

first_num(1,100)
for i in range(1,201):
    if i%3==0 and i%5!=0:
        print("pepsi")
    elif i%5==0 and i%3!=0:
        print("cocacola")
    elif i%3==0 and i%5==0:
        print("fizz")
    else:
        print(i)

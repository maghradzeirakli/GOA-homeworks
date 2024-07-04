def user():

    num = int(input("please enter number: "))
    a = 0

    for i in range(1, num + 1):
        a += i
    print(a)

user()    
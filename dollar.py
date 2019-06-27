while True:
    x = input('How many nodes less than 10 do you want in the game? ')
    try:
        type(int(x)) == type(5)
    except:
        print(x, 'is not an integer type')
    else:
        x = int(x)
        if x <= 10:
            break
        else:
            print(x, 'is not less than 10')

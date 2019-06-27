while True:
    x = input('How many nodes do you want in the game? ')
    try:
        type(int(x)) == type(5)
    except:
        print(x, 'is not an integer type')
    else:
        x = int(x)
        break
print(x, 'is of type {}'.format(type(x)))

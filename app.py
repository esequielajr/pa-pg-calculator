def menu():
    print('Main Menu')
    print('1 - Generate AP')
    print('2 - Generate GP')
    choose = int(input('Type your choose: '))
    if choose == 1:
        generation = generate_ap()
        print(generation)
    elif choose == 2:
        generation = generate_gp()
        print(generation)


def generate_ap():
    ap = [] 
    a1 = int(input('Type the first term of the AP: '))
    r = int(input('Type the common difference: '))
    terms = int(input('Type the number of terms: '))
    while len(ap) < terms:
        ap.append(a1)
        a1+=r
    return ap


def generate_gp ():
    gp = []
    a1 = int(input('Type the first term of the GP: '))
    q = int(input('Type the common ratio of the GP: '))
    terms = int(input('Type the number of terms: '))
    while len(gp) < terms:
        gp.append(a1)
        a1*=q
    return gp

menu()
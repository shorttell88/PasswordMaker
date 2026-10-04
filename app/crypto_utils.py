import random

MyAsciicodeEN = ['!', '?', '"', "'", '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '>', '=', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', '~', 'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','}','|']

MyAsciicodeES = ['!', '¿', '?', '°', '"', "'", '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '' '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '>', '=', '?', '@', 'A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', '~', 'a', 'á', 'b','c','d','e', 'é','f','g','h','i', 'í', 'j','k','l','m','n','o', 'ó', 'p','q','r','s','t','u', 'ú', 'v','w','x','y','z','{','}','|']

def operation(include, normal, appli):
    normal_items = []
    alter_items = []
    theFirst = random.randint(0,100)
    s=0
    j = 0
    if include == 'on':
        for i in normal:
            if j == 0:
                s = (theFirst * 65539 + 2147483648) % len(MyAsciicodeES)
                alter_items.append(s)
                j+=1
            else:
                index_letter = MyAsciicodeES.index(i)
                normal_items.append(index_letter)
                s = (s * 65539 + 2147483648) % len(MyAsciicodeES)
                alter_items.append(s)
    else:
        for i in normal:
            if j == 0:
                s = (theFirst * 65539 + 2147483648) % len(MyAsciicodeEN)
                alter_items.append(s)
                j+=1
            else:
                index_letter = MyAsciicodeEN.index(i)
                normal_items.append(index_letter)
                s = (s * 65539 + 2147483648) % len(MyAsciicodeEN)
                alter_items.append(s)
    
    for i in appli:
        s = (theFirst * 65539 + 2147483648) % len(MyAsciicodeEN)
        alter_items.append(s)
    
    clock = 0
    for i in alter_items:
        clock = clock + i
    Myclock = (clock*len(normal)) % len(MyAsciicodeEN)
    print(len(MyAsciicodeEN))
    alter_items.append(Myclock)


    myFinalResult = ""
    if include == 'on':
        for i in alter_items:
            myFinalResult = myFinalResult + MyAsciicodeES[i]
    else:
        for i in alter_items:
            myFinalResult = myFinalResult + MyAsciicodeEN[i]
    print(normal_items)  
    print(alter_items)
    print(myFinalResult)
    return (myFinalResult, theFirst)

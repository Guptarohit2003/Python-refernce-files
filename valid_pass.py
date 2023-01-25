
a,b,c,d = 0,0,0,0
password = input()
if len(password) in range(6,13):
    for i in password:
        if (i.islower()):
            a+=1
        if (i.isupper()):
            b+=1
        if (i.isnumeric()):
            c+=1
        if (i=='$' or i == '@' or i == '#'):
            d+=1
        
if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d == len(password)):
    print('Valid')
else:
    print("Invalid")


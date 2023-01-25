for _ in range(int(input())):
    s = str(input())
    l = []
    index =3
    for i in range(len(s)-2):
        l.append(s[i:index])
        index +=1
    if "010" in l or "101" in l:
        print("Good")
    else:
        print("Bad")

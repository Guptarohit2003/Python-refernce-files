s = str(input())

for i in range(len(s)):
    if i == 0:
        if s[i].isupper() != True:
            s = s[0].upper() + s[1:]
    if s[i] == " ":
        if s[i+1].isupper() != True:
            s = s[:i+1] + s[i+1].upper() + s[i+2:]             
print(s)
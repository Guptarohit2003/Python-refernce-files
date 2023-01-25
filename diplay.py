x = input()
x = x.lower()
count = 0
vcount = 0
ccount = 0
ncount=0
p =[]
for i in range(0,len(x)):
    if x[i] != ' ':
        count+=1
print("Number of characters are:", count)
li = list(x.split(" "))
print("NUmber of words are:", len(li))
for i in range(0,len(x)):
    if x[i] in ("a","e","i","o","u"):
        vcount+=1
    elif x[i]>='a' and x[i]<='z':
        ccount+=1
print("Number of vowels are:",vcount)
print("Number of consonants are:",ccount)
for i in range(0,len(x)):
    if x[i] >= '1' and x[i]<='9':
        ncount+=1
        p.append(int(x[i]))
print("NUmber of digits are:",ncount)
print("Unique digits are:",set(p))
if sum(p)%2 == 0:
    print("sum is Even")
else:
    print("sum is odd")


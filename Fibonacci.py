n= int(input("Enter the limit:"))
a=0
b=1
print(f"First {n } fibonacci numbers are")

for i in range(n):
    if i==0 or i==1:
        print(i)
    else:
        c=a+b
        a=b
        b=c
        print(c)
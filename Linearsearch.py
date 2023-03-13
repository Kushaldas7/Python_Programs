l=eval(input("Enter the number:"))
x=int(input("Enter the value:"))
f=0
for i in l:
    if i==x:
        f=1
if f==1:
    print("The value isPresent: ")
else:
    print("The value is Not Present: ")

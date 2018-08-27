a=str(input("Enter the name: "))
b=len(a)-1
revstr=""
if len(a)>0:
    for i in a:
        revstr+=(a[b])
        b=b-1
else:
    print("Please Enter the string: ")
print("Reverse string is:",end=" ")
print (revstr)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))

x=int(input("Enter a number whose factorial you want to find:"))
factorial=fact(x)
print("Factorial of %d is : %d"%(x,factorial)) 

if(factorial==120):
    myfile=open('batman.txt')
    print(myfile.read())
else:
    for i in range(1,11):
        print("%d * %d = %d"%(x,i,x*i))

#this a comment

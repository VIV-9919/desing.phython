n= int(input("Enter the number"))
#for i in range(n): # nestead loops
#    for j in range(n):
#        if i==0 or i==n-1 or j==0 or j==n-1:
#            print("*", end=" ")
#        else:
#            print("*", end=" ")
#    print()
#    



#----------Right angle Triangle--------

#for i in range(1, n+1):
#    for j in range(i):
#        print("*", end=" ")
#    print()

#---------Diamond Patten--------

#Upper Triangle
for i in range(1,n+1):
    print(" "*(n-1), end=" ")
    print("* "*i)

# Lower Triangle

for i in range(n-1, 0, -1):
    print(" "*(n-1), end=" ")
    print("* "*i)
        